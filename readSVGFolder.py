"""
Running the "BaseWorkflow" for each SVG inside a folder, folder path is requried when running this function 
"""
import os
import sys
from base_workflow import BaseWorkflow


def readSVGFolder():
    try:
        folder_path = sys.argv[1]
        folders = os.listdir(folder_path)

        with open(folder_path + "/result.txt", "w") as w:
            for i in range(len(folders)):
                f = open(f'{folder_path}/{folders[i]}/svg.txt', 'r')
                svg_string = f.read()
                try:
                    bw = BaseWorkflow(svg_string)
                    alt_text = bw.execute()
                    w.write(f'{folders[i]}: {alt_text}\n')
                except Exception as e:
                    w.write(f'{folders[i]}: {e}\n')
    except:
        print('Please pass directory_name')


if __name__ == '__main__':
    readSVGFolder()
