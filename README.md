# Meme-Stock-Count-from-Reddit-Comment
Work done in Oct. 2021
Grabbed comments related to stock names from wallstreet subreddit, then do a mapreduce job on AWS, finally visualized word counts
1. Set up multi cluster environment
Based on the requirements, i generated 1 master(namenode) with 2 slaves(datanodes)
<img width="146" alt="image" src="https://user-images.githubusercontent.com/69669865/169928054-09989411-1140-4155-a1b3-4f616e70163d.png">
<img width="94" alt="image" src="https://user-images.githubusercontent.com/69669865/169928059-eee24a66-6184-4067-b70c-c4835bd31d9b.png">

2. I  create  a  .py  files  to  collect  data  as  a  json  file  from  Reddit  API,  wallstreetbets  if  be  more 
specific, and convert it to a text file which would be used in mapreduce to count the word search 
in Hadoop soon.
<img width="139" alt="image" src="https://user-images.githubusercontent.com/69669865/169928065-5e270b30-ff26-4549-8ecc-17ee52a584ae.png">
<img width="131" alt="image" src="https://user-images.githubusercontent.com/69669865/169928073-933b7366-7305-4629-a6de-819184d5974d.png">

3. After  mapreducing,  i  got  an  output  which  contains  amount  of  each  stock  mentioned  in  /r 
wallstreetbets,  then  after  simple  data  cleaning,  i  visualized  it  by  a  pie  chart,  a  bar  chat  and  a 
wordcloud in Jupyter Notebook.
Based  on  3  images  above,  on  10/12,2021,  the  most  stock  mentioned  is  SDC  with  12  mentions, 
then ROOT with 10 mentions
<img width="142" alt="image" src="https://user-images.githubusercontent.com/69669865/169928080-52555036-cf21-4353-b8aa-a566de94380c.png">
<img width="216" alt="image" src="https://user-images.githubusercontent.com/69669865/169928086-b69c9545-f5f6-4ec6-87cb-8efc5c5b63cb.png">
<img width="366" alt="image" src="https://user-images.githubusercontent.com/69669865/169928089-dc174c72-7337-4ce3-bb0b-0401a79afc16.png">
