//属性元素

function $(tag,index){
    var elem;
    if(index){
        var elem=document.getElementsByTagName(tag)[index];
        }else{
        elem=document.getElementsByTagName(tag)[0];
        }
        return elem;
}
$("h1",2)