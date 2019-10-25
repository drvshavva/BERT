#!/usr/bin/env python3

#bu fonksiyonda tahmin olasılıkları arasından maksimum beş tahminin
#indisini döndürüyor
def max_n_elemet_indeks(list1): 
    final_list = [] 
  
    for i in range(0, 5):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        
        final_list.append(list1.index(max1)) 
        list1.remove(max1);  
    return final_list