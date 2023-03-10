# SoccerGame環境安裝教學

## 1.新建一個python環境(名稱為SoccerGame-env)。
```
python -m venv SoccerGame-env
```
![image](https://user-images.githubusercontent.com/76472326/212279578-74531445-57eb-4560-8559-24c1ef880859.png)

## 2.進入剛剛所創建的環境中。
```
SoccerGame-env\Scripts\activate
```
![image](https://user-images.githubusercontent.com/76472326/212280113-e25f0f3a-4181-4eb5-97e0-ac9a29c21ef0.png)  
![image](https://user-images.githubusercontent.com/76472326/212280142-0536eabb-ff36-45b3-aeb1-3021b95a3a80.png)


## 3.將ml-agents套件安裝置電腦。
```
git clone -b package --single-branch https://github.com/chi611/MachineLearning-soccergame.git 
```
![image](https://user-images.githubusercontent.com/76472326/212280470-4799ca34-afe8-46bb-a050-bcb78e9abe9f.png)

## 4.進入套件的位置準備進行安裝。
```
cd MachineLearning-soccergame/ml-agents
```
![image](https://user-images.githubusercontent.com/76472326/212282944-f125ad6e-41e4-423b-871d-a71efdc117b0.png)

## 5.開始安裝ml-agents套件。
```
pip install -e .
```
![image](https://user-images.githubusercontent.com/76472326/212284699-180262f3-1605-439a-a813-7badf906bd52.png)  
密密麻麻一大串...  
![image](https://user-images.githubusercontent.com/76472326/212284802-6483dc1b-fe6b-486d-bcf7-bc1b919daefb.png)

## 6.下載gym_unity。  
此時會跳錯誤訊息，是因為我們ml-agents套件是0.28.0，但因為有些套件gym_unity 0.20.0才有，所以我們gym_unity先下載0.20.0再升到0.28.0。
```
pip install gym_unity==0.20.0 
```
![image](https://user-images.githubusercontent.com/76472326/212285110-12c42767-1820-42eb-a446-ef46a83b9a7f.png)

## 7.升級至gym_unity 0.28.0。
```
pip install gym_unity==0.28.0 
```
![image](https://user-images.githubusercontent.com/76472326/212285569-9794b808-7f5f-4da8-8e1b-441bf645e05f.png)

## 8.下載pandas套件  
用來供我們SoccerGame Q-learning查表用。
```
pip install pandas==1.4.2 
```
![image](https://user-images.githubusercontent.com/76472326/212285777-494d66c0-79bc-42fa-896a-0daee92054b2.png)

## 9..keyboard套件  
透過python輸出鍵盤按鍵來操作unity。
```
pip install keyboard==0.13.5 
```
![image](https://user-images.githubusercontent.com/76472326/212286055-787c416f-d608-46a5-851b-3c76653f9782.png)
  

* 此時SoccerGame所需套件已全數安裝完畢，接下來就可以去執行我們SoccerGame的python程式，記得要先進入我們安裝好的環境，再到main.py的位置去執行python
```
SoccerGame-env\Scripts\activate
```
PS:這段指令需與附圖相對的位置才能執行  
![image](https://user-images.githubusercontent.com/76472326/212288609-ab7050b3-b281-4f30-892d-370845475e29.png)
