# 遊戲下載教學  

* 1.先將SoccerGame下載至電腦。
```
git clone -b SoccerGame --single-branch https://github.com/chi611/MachineLearning-soccergame.git 
```
![image](https://user-images.githubusercontent.com/76472326/211967575-2e8c29a6-3fb6-4a60-a793-8ce65b393ad2.png)
  
* 2.於剛剛下載的檔案中輸入"cmd"。  
![image](https://user-images.githubusercontent.com/76472326/211968362-a5c4444f-9257-4e1a-8dc7-a9cf3b44101a.png)

  
* 3.下載python，本次範例是下載3.8.10的python。[python安裝](https://www.python.org/downloads/windows/)  
![image](https://user-images.githubusercontent.com/76472326/211969503-134ce125-0c97-4bf2-a4a3-fd991b9e51ad.png)
  
* 4.新建一個python環境。
```
python -m venv venv 
```
![image](https://user-images.githubusercontent.com/76472326/211970201-2e7d6c8f-e971-430c-a845-1a1f5a933a0d.png)
![image](https://user-images.githubusercontent.com/76472326/211970238-d1886dab-7e8d-4430-9881-0a25255346d3.png)

* 5.進入新創建的環境。
```
venv\Scripts\activate
```
![image](https://user-images.githubusercontent.com/76472326/211971194-0e271d85-bc36-46d0-844b-b9a8d436ec16.png)


* 6.下載gym_unity。(有更新)
```
pip install gym_unity==0.20.0 
```
![image](https://user-images.githubusercontent.com/76472326/211975296-5e260864-afa9-4081-ac01-c8fabc63029a.png)

  
* 7.降低protobuf版本。
```
pip install protobuf==3.20.0 
```
![image](https://user-images.githubusercontent.com/76472326/211971580-daf2ff26-bebe-4ede-ac25-3811054099a4.png)

* 8.下載pandas。
```
pip install pandas==1.4.2 
```
![image](https://user-images.githubusercontent.com/76472326/211972815-d715054f-8725-46f3-bb47-388ce975df09.png)

* 9.下載keyboard
```
pip install keyboard==0.13.5 
```
![image](https://user-images.githubusercontent.com/76472326/211973030-68496eee-b79c-490c-a8a5-04337cb77024.png)
  
  
* 10.執行python(main.py)
```
python main.py
```

