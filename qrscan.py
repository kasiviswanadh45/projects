import qrcode




myqr = qrcode.make("https://www.youtube.com/watch?v=PyDn2gU9DJo&ab_channel=Simplilearn")
myqr1=qrcode.make("https://www.youtube.com/watch?v=dUZTQq_fMWw&ab_channel=StatisticsandDatascience")



myqr.save("myqr.png" , scale =8)
myqr1.save("myqr1.png" , scale =7)

