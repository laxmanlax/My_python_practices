from collections import Counter

def parseweblog(filename):
    items = {}

    with open(filename) as line:
        for data in line:
            host = data.split()[0]
            resCode = data.split()[8]

            if host  not in items:
                items[host] = [resCode]
            else:
                items[host] = items[host] + [resCode]

    return items


def main():
    result = {}
    hosts_res = parseweblog("test.txt")

    for host, code in hosts_res.items():
        result[host] = Counter(code)

    allhosts = sorted(result.items(), key=lambda x:x[1]['200'])
    print allhosts


if __name__=="__main__":
    main()
