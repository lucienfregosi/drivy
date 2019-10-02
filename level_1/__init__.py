import os
import sys
import json
import lib as l

# Level 1

def main():
    try:
        ## Variables ##
        current_path = os.path.abspath(os.path.dirname(__file__))
        log_folder_path_input = '../logs'
        log_folder_path_output = '../parsed'
        directory_input = os.fsencode(log_folder_path_input)
        path_directory_input = current_path + "/" + log_folder_path_input
        path_directory_output = current_path + "/" + log_folder_path_output

        # Create output folder if not exist
        if not os.path.exists(path_directory_output):
            os.makedirs(path_directory_output)
        
        ## Script ##
        for fileDir in os.listdir(directory_input):
            filename = os.fsdecode(fileDir)
            print(filename)
            # Open
            file = open(path_directory_input + "/" + filename, "r")
            content = file.read()
            # Process
            dict_output = l.convertStringToDict(content)
            # Write
            with open(path_directory_output + "/" + filename.replace("txt","json"), 'w') as json_file:
                json.dump(dict_output, json_file, indent=4)
            # Delete Original File
            file.close()
            os.remove(path_directory_input + "/" + filename)
    except:
        print(sys.exc_info()[0]," occured.")
        sys.exit()
        



if __name__ == '__main__':
    main()

    
