$(function () {

    // Globals

    function loadVideo() {
	
	alert("Loading video...");
	/*$.ajax({
	    type: "GET",
	    url: "/play_video?imgfile="+curr_file,
	    data: {'message':'message'},
	    
	    success:function(resp) {
		if (resp.success > 0) {
		    
		    // Standard Implementation
		    img = new Image();
		    img.src = "data:image/png;base64," + resp.imagefile;
		    //img.src = "data:image/jpeg;base64," + resp.imagefile;

		    // New
		    img.onload = function () {
			resizeCanvas();
			imgarr = resp.imgarr;
			initCanvas();
		    }
		    
		    $("#VIEW").html(resp.view);
		    //alert("SUCCESS for file: "+curr_file);
		} else {
		    alert("Sorry, there was an error finding the submitted video. Ensure that the video is the proper MP$ format.");
		}
		removeImages();
	    }
	}); */
    }

   $("#loadVideoButton").on("click",function(e) {
       e.preventDefault();
       var player = jwplayer("myVideoPlayer");
       if (player.length == 1) {
           player = player[0];                          
           player.sendEvent("LOAD", "https://s3.amazonaws.com/rayvids/TestVideo.mp4");
       }
       loadVideo();
    }); 

    function removeImages () {
	var dropbox = $('#dropbox'),
	message = $('.message', dropbox);
	$('.preview').remove();
	message.show();
	curr_url = [];
    }
    
    // resize the canvas to fill browser window dynamically
    //window.addEventListener('resize', resizeCanvas, false); 

});