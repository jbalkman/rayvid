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

   $("#example-6").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase6.mp4", image:"/content/Slide6.jpg"}]);
   });

   $("#example-7").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase7.mp4", image:"/content/Slide7.jpg"}]);
   });

   $("#example-8").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase8.mp4", image:"/content/Slide8.jpg"}]);
   });

   $("#example-9").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase9.mp4", image:"/content/Slide9.jpg"}]);
   });

   $("#example-10").on("click",function(e) {
       e.preventDefault();
       jwplayer("myVideoPlayer").load([{file:"/content/BreastCase10.mp4", image:"/content/Slide10.jpg"}]);
   });

});