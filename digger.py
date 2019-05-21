# coding: utf-8
import os


def get_files(file_format='.log'):
    files = []
    current_path = os.getcwd()
    for filename in os.listdir(current_path):
        if filename.endswith(file_format):
            files.append(filename)
    return files


def parse_endpoint(origin): 
    origin = origin.split('?')[0]
    origin = origin.split('/')
    result = []
    for chunk in origin:
        try:
            chunk = int(chunk)
            result.append('{int}')
        except ValueError:
            result.append(chunk)
    return '/'.join(result)


def parse_log(line):
    line = line.split('"')[1]
    method, endpoint, _ = line.split()
    return f'{method} {parse_endpoint(endpoint)}'


def dig_log_files(files):
    result = {}
    for filename in files:
        print(filename)
        with open(filename) as f:
            for line in f:
                endpoint = parse_log(line)
                if endpoint in result:
                    result[endpoint] += 1
                else:
                    result[endpoint] = 1
    return result   


if __name__ == '__main__':
    files = get_files()
    data = dig_log_files(files)

    data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    print(data)

