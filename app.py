<!DOCTYPE html>
<html>
<head>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- Optional theme -->
<!-- <link rel="stylesheet" href="D:\For sachin\adam\resources\bootstrap-3.2.0\dist\css\bootstrap-theme.min.css"> -->
<link rel="script" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js">

<!-- Latest compiled and minified JavaScript 
<script src="D:\For sachin\adam\resources\bootstrap-3.2.0\dist\js\bootstrap.min.js"></script>-->

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script>
var displayIpMessage = function(msg){
	var el = '<li class="left clearfix">    <span class="chat-img pull-left"> <img src="http://placehold.it/50/55C1E7/fff&text=U" alt="UserAvatar" class="img-circle" />    </span>    <div class="chat-body clearfix">         <div class="header">             <strong class="primary-font">Adam</strong> <small class="pull-right text-muted">                <span class="glyphicon glyphicon-time"><span>12mins ago</small>        </div>        <p class="content">            '+msg+'        </p>    </div></li>'
	$(el).appendTo(".chat");
$('.panel-body').animate({ scrollTop: 		$('.panel-body').prop('scrollHeight')}, 1000);
}
var displayOpMessage = function(msg){
	var el = '<li class="right clearfix">    <span class="chat-img pull-right">        <img src="http://placehold.it/50/FA6F57/fff&text=ME"alt="User Avatar" class="img-circle" />    </span>    <div class="chat-body clearfix">        <div class="header">           <small class=" text-muted"><span class="glyphicon glyphicon-time"></span>13 mins ago</small>            <strong class="pull-right primary font">You</strong>        </div>        <p class="content pull-right">            '+msg+'        </p>    </div></li>'
	$(el).appendTo(".chat");
	$('.panel-body').animate({ scrollTop: 		$('.panel-body').prop('scrollHeight')}, 1000);
}
var send = function(){
	var msg = document.getElementById("btn-input").value;
	displayIpMessage(msg);
        document.getElementById("btn-input").value = "";
	$.get("http://127.0.0.1:5000/get/" + msg, function(data, status){
        displayOpMessage(data);
    });
}
$(document).keypress(function(e) {
    if(e.which == 13) {
        send();
    }
});
</script>
<style>
.container
{
	position: absolute;
    bottom: 0;
    left: 0;
}
.chat
{
    list-style: none;
    margin: 0;
    padding: 0;
}
.chat li
{
    margin-bottom: 10px;
    padding-bottom: 5px;
    border-bottom: 1px dotted #B3A9A9;
}
.chat li.left .chat-body
{
    margin-left: 60px;
}
.chat li.right .chat-body
{
    margin-right: 60px;
}
.chat li .chat-body p
{
    margin: 0;
    color: #777777;
}
.panel .slidedown .glyphicon, .chat .glyphicon
{
    margin-right: 5px;
}
.panel-body
{
    overflow-y: scroll;
    height: 250px;
}
::-webkit-scrollbar-track
{
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    background-color: #F5F5F5;
}
::-webkit-scrollbar
{
    width: 12px;
    background-color: #F5F5F5;
}
::-webkit-scrollbar-thumb
{
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
    background-color: #555;
}
</style>
</head>

<body>

<div>
<h1>Adam is live...</h1>
</div>

<div class="container">
    <div class="row">
        <div class="col-md-5">
            <div class="panel panel-primary">
                <div class="panel-heading" id="accordion">
                    <span class="glyphicon glyphicon-comment"></span> Talk to adam here...
                    <div class="btn-group pull-right">
                        <a type="button" class="btn btn-default btn-xs" data-toggle="collapse" data-parent="#accordion" href="#collapseOne">
                            <span class="glyphicon glyphicon-chevron-down"></span>
                        </a>
                    </div>
                </div>
            <div class="panel-collapse" id="collapseOne">
                <div class="panel-body">
                    <ul class="chat">
                    </ul>
                </div>
                <div class="panel-footer">
                    <div class="input-group">
                        <input id="btn-input" type="text" class="form-control input-sm" placeholder="Type your message here..." />
                        <span class="input-group-btn">
                            <button class="btn btn-warning btn-sm" id="btn-chat" onclick="send()">
                                Send</button>
                        </span>
                    </div>
                </div>
            </div>
            </div>
        </div>
	</div>
</div>


</body>
</html>
