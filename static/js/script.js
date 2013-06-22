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

    /**
     * カテゴリからサブカテゴリを取得する
     */
    $("#id_category").change( function(){
        $.ajax({
               url: "/manage/ajax/book_subcategory/",
               type: 'GET',
               data: {"category_id": $(this).val()},
               dataType: 'text',
               async: false,
               global: true,
               success: function(rt){
                           subcategory = rt.replace(/\|/ig, "\n");
                           $('#id_subcategory').children().remove();
                           $('#id_subcategory').append(subcategory);        
                        }
              })
    });

    /**
     * サブカテゴリからタイトルを取得する
     */
    $("#id_subcategory").change( function(){
        $.ajax({
               url: "/manage/ajax/book_title/",
               type: 'GET',
               data: {"subcategory_id": $(this).val()},
               dataType: 'text',
               async: false,
               global: true,
               success: function(rt){
                           title = rt.replace(/\|/ig, "\n");
                           $('#id_book').children().remove();
                           $('#id_book').append(title);        
                        }
              })
    });

    /**
     * タイトルからvolumeを取得する
     */
    $("#id_book").change( function(){
        $.ajax({
               url: "/manage/ajax/book_volume/",
               type: 'GET',
               data: {"book_id": $(this).val()},
               dataType: 'text',
               async: false,
               global: true,
               success: function(rt){
                           volume = rt.replace(/\|/ig, "\n");
                           $('#id_volume').children().remove();
                           $('#id_volume').append(volume);        
                        }
              })
    });

    /**
     * カテゴリから著者を取得する
     */
    $("#id_category").change( function(){
        $.ajax({
               url: "/manage/ajax/book_writer/",
               type: 'GET',
               data: {"category_id": $(this).val()},
               dataType: 'text',
               async: false,
               global: true,
               success: function(rt){
                           writer = rt.replace(/\|/ig, "\n");
                           $('#id_writer').children().remove();
                           $('#id_writer').append(writer);        
                        }
              })
    });


    /**
     * カテゴリから出版会社を取得する
     */
    $("#id_category").change( function(){
        $.ajax({
               url: "/manage/ajax/book_publisher/",
               type: 'GET',
               data: {"category_id": $(this).val()},
               dataType: 'text',
               async: false,
               global: true,
               success: function(rt){
                           publisher = rt.replace(/\|/ig, "\n");
                           $('#id_publisher').children().remove();
                           $('#id_publisher').append(publisher);        
                        }
              })
    });


    /**
     *  クリックしたら消える文字の処理
     */
    // 初期値の文字色
    var d_color = '#707070';
    // 通常入力時の文字色
    var f_color = '#000';
     
    // Searchフォーム
    $(".searchText").css('color', d_color).focus(function(){
        if(this.value == this.defaultValue){
            this.value = '';
            $(this).css('color', f_color);
        }
    })

});
