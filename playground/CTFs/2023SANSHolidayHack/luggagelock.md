for(a=0;a<10;a++)for(b=0;b<10;b++)for(c=0;c<10;c++)for(d=0;d<10;d++)socket.emit('message',{
"Type":"Open","Combo":""+a+b+c+d });