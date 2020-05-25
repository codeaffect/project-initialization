import sys
import json

#global variables
gv = ["l", "rn", "d"]
lang = ""
repo_name = ""
fp = ""


def GetEnvironmentSettings():
    # read file
    with open('env.json', 'r') as env_file:
        data = env_file.read()

    # parse file
    obj = json.loads(data)

    # show values
    for j in obj:
        key = str(j)
        print(key + ':'+obj[key])


def GetValue(param_value):
    # split param_value by ':'
    print('value:', param_value.split(':'))


def main():
    # get params
    params = sys.argv

    # load Environment Variables
    GetEnvironmentSettings()

    # getValue
    GetValue(params[1])

    values = [p for p in params
              for v in gv
              if p.startswith(v)]

    print(*values)


if __name__ == '__main__':
    main()
