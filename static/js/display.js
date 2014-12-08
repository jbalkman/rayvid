$(function(){

   $("#example-1").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase1.mp4", image:"/content/Slide1.jpg"}]);
       //jwplayer("myVideoPlayer").setup([{file:"/content/Example.mp4"}]); // try setup?
   }); 

   $("#example-2").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase2.mp4", image:"/content/Slide2.jpg"}]);
   }); 

   $("#example-3").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase3.mp4", image:"/content/Slide3.jpg"}]);
   }); 

   $("#example-4").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase4.mp4", image:"/content/Slide4.jpg"}]);
   }); 

   $("#example-5").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase5.mp4", image:"/content/Slide5.jpg"}]);
   });

});