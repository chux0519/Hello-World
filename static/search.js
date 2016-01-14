// search
var keyword="";
function map(){
    keyword= $.trim($("#keyword").val());
    if (keyword==''){
        alert('请输入药品种类');
        $("#keyword").focus();
        return false;
    }    $.ajax({
        url:"/map",
        type:'GET',
        dataType:'json',
        data:{"id":$("#keyword").val()},
        success:function (data)
        {
            if(data==''){alert('没有此药信息！');return false;}
            var re="<br><hr><p>";
            $.each(data,function(i,item){
                alert('收到数据');
                re+="药理分类一:"+ item.yaoli1 +"<br>";
            re+="</p>";
            // document.write(re.replace(/null/g,"无"))
            document.getElementById("result").innerHTML=re.replace(/null/g,"无");
            // echo re;
            // $('#result').html(re);
            })
        },
        erro:function()
        {
            alert('不存在的药物！');
        }
    })
}
