# SocieteGeneralApplication
Download all files.
In Terminal:
 - cd into directory "SocietyGeneraleTest_Karim"
 - Add permissions to run: chmod +x ./SocietyGeneralTest.bash
 - run script : " ./SocietyGeneralTest.bash"
 - This will execute q1.py to show retrieval from yahoo finance api as well as calculate the notional (product of quantity and the closing price of passed stock/label)
 
 - You can edit the Label (stock) and the quantity by modifying paramters within the call for method: "current_market_value(2400,'TSLA')"

 - Script will also run the flask environment and host an api locally on your machine. 
 - You will be able to input parameters in your url like so :http://127.0.0.1:5000/123/AMZN where 123 and AMZN are the parameters and you will receive the notional (product of quantity 123 * the closing price of AMZN)
