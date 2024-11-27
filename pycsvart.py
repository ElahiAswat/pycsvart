import cv2
import numpy as np
import csv

csv_path="/files/test.csv"
image_path="/files/test.jpg"

image=cv2.imread(image_path)

def text(int):
     if int==0:
         return ""
     else:
         return " "
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 0, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for y in range(binary.shape[0]):
            row = []
            for x in range(binary.shape[1]):
                     diff = text(binary[y, x])
                     row.append(diff)
            writer.writerow(row)
'''
i=0
for y in range(binary.shape[0]):
    for x in range(binary.shape[1]):
            i=i+1
            print(i)           
            
print(x*y)'''

        
                        
       

 
                               
                


