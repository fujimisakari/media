
// // マウスをのせた時のタグの挙動
// function rollover()
// {
//   if(!document.getElementById || !document.createTextNode){return;}
//   var n=document.getElementById('manageNavi');
//   if(!n){return;}
//   var lis=n.getElementsByTagName('li');
//   for (var i=0;i<lis.length;i++)
//   {
//     lis[i].onmouseover=function()
//     {
//       this.className=this.className?'cur':'over';
//     }
//     lis[i].onmouseout=function()
//     {
//        this.className=this.className=='cur'?'cur':'';
//     }
//   }
// }

// // テーブルで1行おきに背景色を変える
// function tableZebra() {
//     var classN = "manageList";     //クラス名を指定
//     var addClass1 = "trcolor1";    //奇数タグのクラス名を指定
//     var addClass2 = "trcolor2";    //偶数タグのクラス名を指定

//     if (!document.getElementsByTagName) return false;
 
//     var zebraTables = document.getElementsByTagName("table");
    
//     for (var i=0; i < zebraTables.length; i++) {
//         if (zebraTables[i].className.match(classN)) {
 
//             var zebraRows = zebraTables[i].getElementsByTagName("tr");
            
//             for (var k=0; k < zebraRows.length; k++) {
//                 if (k%2) {
//                     zebraRows[k].className = addClass2;
//                 } else {
//                     zebraRows[k].className = addClass1;
//                 }
//             }
//         }
//     }
// }
// window.onload = function() { rollover(); tableZebra(); }

/**
 * ajax処理
 */
$(document).ready(function() {

    /**
     * サムネイル画像を拡大表示する
     */
    $("a.thumbnail_view").fancybox({
            'opacity'       : true,
            'transitionIn'  : 'elastic',
            'transitionOut' : 'none',
            'overlayColor'  : '#000',
            'overlayOpacty' : '0.9'
    });

    // /**
    //  * カテゴリからサブカテゴリを取得する
    //  */
    // $("#id_category").change( function(){
    //     $.ajax({
    //            url: "/manage/ajax/book_subcategory/",
    //            type: 'GET',
    //            data: {"category_id": $(this).val()},
    //            dataType: 'text',
    //            async: false,
    //            global: true,
    //            success: function(rt){
    //                        subcategory = rt.replace(/\|/ig, "\n");
    //                        $('#id_subcategory').children().remove();
    //                        $('#id_subcategory').append(subcategory);        
    //                     }
    //           })
    // });

    // /**
    //  * サブカテゴリからタイトルを取得する
    //  */
    // $("#id_subcategory").change( function(){
    //     $.ajax({
    //            url: "/manage/ajax/book_title/",
    //            type: 'GET',
    //            data: {"subcategory_id": $(this).val()},
    //            dataType: 'text',
    //            async: false,
    //            global: true,
    //            success: function(rt){
    //                        title = rt.replace(/\|/ig, "\n");
    //                        $('#id_entry').children().remove();
    //                        $('#id_entry').append(title);        
    //                     }
    //           })
    // });

    // /**
    //  * タイトルからvolumeを取得する
    //  */
    // $("#id_entry").change( function(){
    //     $.ajax({
    //            url: "/manage/ajax/book_volume/",
    //            type: 'GET',
    //            data: {"book_id": $(this).val()},
    //            dataType: 'text',
    //            async: false,
    //            global: true,
    //            success: function(rt){
    //                        volume = rt.replace(/\|/ig, "\n");
    //                        $('#id_volume').children().remove();
    //                        $('#id_volume').append(volume);        
    //                     }
    //           })
    // });

    // /**
    //  * カテゴリから著者を取得する
    //  */
    // $("#id_category").change( function(){
    //     $.ajax({
    //            url: "/manage/ajax/book_writer/",
    //            type: 'GET',
    //            data: {"category_id": $(this).val()},
    //            dataType: 'text',
    //            async: false,
    //            global: true,
    //            success: function(rt){
    //                        writer = rt.replace(/\|/ig, "\n");
    //                        $('#id_writer').children().remove();
    //                        $('#id_writer').append(writer);        
    //                     }
    //           })
    // });

    /**
     *  クリックしたら消える文字の処理
     */
    // 初期値の文字色
    var d_color = '#d9d9d9';
    // 通常入力時の文字色
    var f_color = '#FAFAD2';
     
    // Searchフォーム
    $("input.id_search").css('color', d_color).focus(function(){
        if(this.value == this.defaultValue){
            this.value = '';
            $(this).css('color', f_color);
        }
    })

});
