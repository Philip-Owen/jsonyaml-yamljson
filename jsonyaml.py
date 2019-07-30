import yaml, json, sys
from os import listdir, path, mkdir

def setOutputPath(counter=1):
    
    if counter == 3:
        print("Your input is invalid. Please verify input and or path and try again")
        sys.exit()

    setPath = input("\nConverted files, by default, are stored in the ./output folder. Would you like to specify a different folder? y/n \n> ")

    if setPath.lower() in ('no', 'nope', 'n'):
        return './output'
    elif setPath.lower() in ('yes', 'ye', 'y'):
        newPath = input('Please specify the path. If the path does not yet exist it will be created > ')
        if not path.isdir(newPath):
            mkdir(newPath)
        return newPath
        
    else:
        print(f'{setPath} is not an option. Please try again')
        getFilePath(counter+1)

def getFilePath(type, counter=1):

    if counter == 3:
        print("Your input is invalid. Please verify input and try again")
        sys.exit()

    fileLocation = input(f"\n\nAre the files you want to convert in the ./{type} folder?  y/n\n> ")

    if fileLocation.lower() == 'y':
        return f'./{type}'
    elif fileLocation.lower() == 'n':
        userPath = input('Please specify the path > ')
        return userPath
    else:
        print(f'{fileLocation} is not a valid input. Please try again')
        getFilePath(type, counter+1)

def converFiles(outputPath, fileType):

    dirPath = getFilePath(fileType)
    if fileType == 'yaml':
        files = filter(lambda f: f.endswith((f'.{fileType}', '.yml')), listdir(dirPath))
    else:
        files = filter(lambda f: f.endswith(f'.{fileType}'), listdir(dirPath))

    for file in files:
        fromFile = open(f'{dirPath}/{file}', 'r')
        fileName = file.split(f'.{fileType[0]}')[0]

        if fileType == 'json':
            newFile = f'{outputPath}/{fileName}.yaml'
            with open(newFile, 'w') as f:
                yaml.dump(json.load(fromFile), f, indent=4, sort_keys=False)
        else:
            newFile = f'{outputPath}/{fileName}.json'
            with open(newFile, 'w') as f:
                json.dump(yaml.safe_load(fromFile), f, indent=4, separators=(',', ': '))

    print('File conversion completed...')


def main():
    outPath = setOutputPath()

    if len(sys.argv) == 1:
        print("""
            You must provide a file format argument.

            For converting JSON files to YAML use --json
            For converting YAML files to JSON use --yaml

        """)
        sys.exit()
    else:
        if sys.argv[1] == '--json':
            converFiles(outPath, 'json')
        elif sys.argv[1] == '--yaml':
            converFiles(outPath, 'yaml')
        else:
            print(f"""
            Sorry, {sys.argv[1]} is not a valid argument...

            For converting JSON files to YAML use --json
            For converting YAML files to JSON use --yaml
            """)
    
    sys.exit()



if __name__ == '__main__':
    main()