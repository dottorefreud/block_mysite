import hashlib
import base58
import binascii
import getall

#открываем файл с тектом
def text_to_address(x):
    #with open('text_in_address.txt', 'rb') as f:
    #text_from_file = f.read()#читаем его весь в одну строку
    #print(text_from_file)
    
   
#переводим строку 1 в байты и отображаем байты в HEX
#декодируем в строку для дальнейшей работы с HEX как строкой
    txt = binascii.hexlify(x.encode()).decode()
    #print(txt)
#получаем разбитие по 20 байт (40 символов в HEX)
    list_text = [txt[i:i+40] for i in range(0, len(txt), 40)]
    #print(list_text)
# предыдущее разбитие собираем в список
#перед этим проверяем не меньше ли 20 быйт
#затем применяем двойное ша256 шифрование и берем первые 4 байта(8 символов)
#кодируем результат контатации в биткоин адреса

    list_40 = []
    for i in list_text:
        while len(i) < 40:
            i = i + '2a'
    #print(i)
    #print('00' + i)
       
    
        wsha256 = getall.whash256('00' + i)
        #print(wsha256)
        address_hex = '00' + i + wsha256
        address_base58 = base58.b58encode(bytes.fromhex(address_hex))
        list_40.append(address_base58)
#print(list_40)
#записываем адреса в файл каждый с новой строки
    #file_address = open('address2.txt', 'w')
    #for i in list_40:
        #file_address.write(i + '\n')
    #file_address.close()
    return(list_40)
        






