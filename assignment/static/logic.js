let flag = true;
let falgColl = true;

$(document).ready(function () {
  $(".product-top,.hidden-alt").hover(function () {
    flag ? $(".hidden-alt").show() : $(".hidden-alt").hide();
    falgColl
      ? $(".coll").trigger("click") //pass;
      : (flag = !flag);
    falgColl = false;
  });
});
