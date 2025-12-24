# 計算機概論期末報告
物理實驗數據分析工具
* **姓名：** 陳宥昕
* **學號：** B14504116
## 1 程式的原理與功能
這個程式的功能，是在幫助處理物理實驗裡面麻煩的大量數據分析，可以把數字輸入後自動輸出結果，但局限於所求的數值是實驗測量值之間加減乘除後得到的結果，像是克特-可倒擺。
程式需要用到兩個插件，numpy跟scipy
我們需要先輸入公式，接著辨認公式中的變數，以利後續的計算
輸入數據和儀器最小刻度後，會進行兩部分，分別是最佳值與不確定度的計算
一個一個輸入數據後，計算平均值
輸入儀器最小刻度計算b類不確定度($\frac{a}{\sqrt{12}}$)，以及利用前面的數據得出標準差($\sqrt{\sum_{i=1}^{n} \frac{\left(x_{i}-\mu\right)^{2}}{n-1}}$)後再除以$1\sqrt{n}$得出a類不確定度，u_c便可由($\sqrt{u_a^2+u_b^2}$)得出。
接著需將各個變數的不確定度套入不確定度傳遞公式，公式如下
<img width="364" height="155" alt="螢幕擷取畫面 2025-12-23 234709" src="https://github.com/user-attachments/assets/dae4eae8-f35c-40e2-8791-40f7e1a94ed1" />
所以我們必須計算各個變數在原函數偏微分後的結果，再將其函數值(也就是前面的平均值)和不確定度代入後，平方相加後開根號便能得到總的不確定度。
最後再把數值輸出就可以了。
## 2 使用方式
一開始需要用python的語法把所球的公式輸入。舉例來說，($\frac{4\pi^2}{P^2} \times(l_1+l_2)$)就要打4*pi**2/(P**2*(l1+l2)。

多個變數各自的平均值和不確定度可用歉面分離出的變數，套入for迴圈並利用dictionary將各自的數值紀錄起來。
<img width="437" height="191" alt="螢幕擷取畫面 2025-12-24 173403" src="https://github.com/user-attachments/assets/493b9271-0175-4c5f-90e0-f7258cb5f3ad" /><img width="629" height="134" alt="螢幕擷取畫面 2025-12-24 173426" src="https://github.com/user-attachments/assets/0c61e525-2b1e-465f-bd66-ccc5af5d789f" /><img width="426" height="317" alt="螢幕擷取畫面 2025-12-24 173445" src="https://github.com/user-attachments/assets/96cce214-287d-4760-875a-084d760f43e7" /><img width="622" height="239" alt="螢幕擷取畫面 2025-12-24 173356" src="https://github.com/user-attachments/assets/5cf1b892-252f-4283-81fa-a3d072ddfefc" />



/>



## 3 程式的架構
## 4 開發過程
## 5 參考資料來源
## 6 程式修改或增強的內容
