var l_text=function (select_object){
    $.ajax(
        {
            type: "post",
            url: "info/all",
            data:"",
            dataType:"json",
            success:function (data){
                var option=""
                $.each(data,function (index,menu){
                    option+=""
                })
                $("#parent_id").html(option)
            }
        }
    )
}