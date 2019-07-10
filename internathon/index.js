$.ajax({
    url : "http://127.0.0.1:8000/get_posts",
    type : "GET",
    dataType: "json",
    success : function(json) {
        alert(json['posts'][0]['post_id']);
        // $('#result').append( 'ServerResponse:' + json.server_response);
    },
    error : function(xhr,errmsg,err) {
        alert(xhr.status + ": " + xhr.responseText);
    }
});

$.ajax({
    url : "http://127.0.0.1:8000/set_posts",
    type : "POST",
    dataType: "json",
    data : {
        'post_id':'4',
        'post_caption':'jab tak hai jaan',
        'lp':'ab kya hoga',
        'likes':'40',
        'post_url':'dnjdkns',
        },
    success : function(json) {
        // $('#result').append( 'ServerResponse:' + json.server_response);
    },
    error : function(xhr,errmsg,err) {
        alert(xhr.status + ": " + xhr.responseText);
    }
});

