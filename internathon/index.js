$.ajax({
    url : "http://127.0.0.1:8000/get_posts",
    type : "GET",
    dataType: "json",
    success : function(json) {
console.log(json['posts']);
for(var i in json['posts']){
console.log(i);
var v=json['posts'][i]['post_url']
var vv=json['posts'][i]['post_caption']
var vvv=json['posts'][i]['lp']
var div_text='<div class="card" style="width:800px;margin-bottom: 10%;"><img class="card-img-top" src="'+v+'" alt="Card image" style="width:100%" id="1"><div class="card-body"><h4 class="card-title">John Doe</h4><p class="card-text">'+vv+'<br>#'+vvv+'</p><i onclick="myFunction(this)" class="fa fa-thumbs-up" id="test"></i></div></div>'
document.getElementById("putshithere").innerHTML=document.getElementById("putshithere").innerHTML+div_text;
}
        // $('#result').append( 'ServerResponse:' + json.server_response);
    },
    error : function(xhr,errmsg,err) {
       // alert(xhr.status + ": " + xhr.responseText);
    }
});
$.ajax({
    url : "http://127.0.0.1:8000/set_posts",
    type : "POST",
    dataType: "json",
    data : {
        'post_id':'1',
        'post_caption':'eno ondhu',
        'lp':'bias for action',
        'likes':'40',
        'post_url':"bisibelebath",
        },
    success : function(json) {
         window.location.href="http://localhost:63342/internathon/internathon.html"
    },
    error : function(xhr,errmsg,err) {
//        alert(xhr.status + ": " + xhr.responseText);
    }
});


