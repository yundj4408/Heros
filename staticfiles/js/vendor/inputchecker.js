function inputChecker(){
        if(inputForm.categorie.value == "게시판선택"){
            alert("카테고리를 골라주세요");
            return false;
        }
        if(inputForm.title.value.length<1){
            alert("제목을 입력하세요");
            return false;
        }
        if(inputForm.place.value.length<1){
            alert("장소를 입력하세요");
            return false;
        }
        if(inputForm.price.value.length<1){
            alert("금액을 입력하세요");
            return false;
        }
        if(inputForm.text.value.length<1){
            alert("내용을 입력하세요");
            return false;
        }
    }