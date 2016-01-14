// var str = ${.content};
// function HightLight(e){ var reg = new RegExp(e, 'g')
// str = str.replace(reg, function(v){ return v.fontcolor('Red') });
//    } 
// HightLight('药品名称') 
// HightLight('生产企业') 
// document.write(str);
// document.getElementById("content").innerHTML=re.replace(/null/g,function(v){ return v.fontcolor('Red') });
// function Map_Master_Slave(){
// 	var master_arr=new Array();
// 	var slave_arr=new Array();
// 	var checkboxs = document.getElementById("slave_checkbox");	
// 	//id是唯一的，多选一定要用document.getElementsByName
// 	alert('got checkboxs')
// 	for (var i = 0 ;i<checkboxs.length;i++){
// 		if (checkboxs[i].checked==true){
// 			alert('i');
// 			master_arr.push(checkboxs[i].name);
// 			slave_arr.push(checkboxs[i].value);
// 			alert(checkboxs[i].value);
// 		}
// 	}
// }

function Map_Master_Slave(){
	var master_arr=new Array();
	var slave_arr=new Array();
	var checkboxs = document.getElementsByName("slave_checkbox");
	alert(checkboxs.length);
	for (var i = 0 ;i<checkboxs.length;i++){
		if (checkboxs[i].checked){
			alert(i);
			master_arr.push(checkboxs[i].id);
			slave_arr.push(checkboxs[i].value);
			alert(checkboxs[i].value);
		}
	}
	$.post("/map",
	{
		master_id:master_arr;
		slave_id:slave_arr;
	},
	function(status){
		alert("您的操作"+status);
	}
		)
	}
	}
}