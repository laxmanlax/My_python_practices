package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strings"

	"github.com/gorilla/mux"
)

// Config Struct (Model)
type Config struct {
	Name     string                 `json:"name"`
	Metadata map[string]interface{} `json:"metadata"`
}

var allconfigs []Config

// Get all configs
func getConfigs(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(allconfigs)
}

// Get one configs
func getConfig(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r) // Gets params
	// Loop through books and find one with the id from the params
	for _, item := range allconfigs {
		if item.Name == params["name"] {
			json.NewEncoder(w).Encode(item)
			return
		}
	}
	json.NewEncoder(w).Encode(&Config{})
}

// Add configs
func addConfigs(w http.ResponseWriter, r *http.Request) {
	var config Config
	jsonByte, err := ioutil.ReadAll(r.Body)
	err = json.Unmarshal(jsonByte, &config)
	if err != nil {
		log.Fatal(err)
	}
	_ = json.NewDecoder(r.Body).Decode(&config)
	allconfigs = append(allconfigs, config)
	json.NewEncoder(w).Encode(config)

}

// Delete config
func deleteConfigs(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	for index, item := range allconfigs {
		if item.Name == params["name"] {
			allconfigs = append(allconfigs[:index], allconfigs[index+1:]...)
			break
		}
	}
	json.NewEncoder(w).Encode(allconfigs)
}

// Update configs
func updateConfig(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	for index, item := range allconfigs {
		if item.Name == params["name"] {
			allconfigs = append(allconfigs[:index], allconfigs[index+1:]...)
			var config Config
			_ = json.NewDecoder(r.Body).Decode(&config)
			allconfigs = append(allconfigs, config)
			json.NewEncoder(w).Encode(config)
			return
		}
	}
}

// Query Configs
func queryConfigs(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := r.URL.Query()
	var str1 = params.Encode()
	split1 := strings.Split(str1, "=")
	query := strings.Split(split1[0], ".")

	s := query[len(query)-1]
	//fmt.Println("parms -- ", split1[1])

	for _, item := range allconfigs {

		for _, value := range query[1:] {

			//fmt.Println("query -- ", value)

			f := item.Metadata[value]
			//fmt.Println("query result -- ", f)
			switch f := f.(type) {

			case map[string]interface{}:
				for k, v := range f {

					switch vv := v.(type) {
					case string:
						{
							//fmt.Println("query", value, " key :  resul", k, v)
							if k == s && v == split1[1] {
								json.NewEncoder(w).Encode(item)
								break
							}
						}
					case interface{}:
						md, ok := vv.(map[string]interface{})
						fmt.Println("result -- ", md[value], ok)

					}

				}

			}

		}

	}
}

func main() {

	// Init Router
	r := mux.NewRouter()
	port := os.Getenv("SERVER_PORT")
	// fmt.Println("SERVE_PORT   :", port)
	// Route Handlers / Endpoints
	r.HandleFunc("/configs", getConfigs).Methods("GET")
	r.HandleFunc("/configs", addConfigs).Methods("POST")
	r.HandleFunc("/configs/{name}", getConfig).Methods("GET")
	r.HandleFunc("/configs/{name}", updateConfig).Methods("PUT")
	r.HandleFunc("/configs/{name}", deleteConfigs).Methods("DELETE")
	r.HandleFunc("/search", queryConfigs).Methods("GET")
	log.Fatal(http.ListenAndServe(port, r))

}
