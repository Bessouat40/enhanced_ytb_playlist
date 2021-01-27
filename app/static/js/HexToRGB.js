function HexToRGB(hex_color,trnsprnc){

	  var myRegexp = /#+([a-zA-Z0-9]{2})+([a-zA-Z0-9]{2})+([a-zA-Z0-9]{2})/gm;
	  var m = myRegexp.exec(hex_color);
	  var r = parseInt(m[1],16);
	  var g = parseInt(m[2],16);
	  var b = parseInt(m[3],16);
	  
	  return( "rgb("+r+","+ g+","+b+","+trnsprnc+")")

	}