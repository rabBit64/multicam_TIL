document.forms[0].addEventListener("submit", function(e){
  //1. 폼 전송 이벤트 취소
  e.preventDefault();
  const idEl = document.forms[0].username;
  const idValue = document.forms[0].value.trim();
  const pwEl = document.forms[0].password;
  const pwValue = document.forms[0].value.trim();

  //2. 아이디가 입력되었는지 확인, 입력되지 않았으면 경고창 표시, 포커스 이동
  if(idValue==""){
    alert("아이디를 입력해 주세요");
    idEl.focus();
    return;
  }
  //3. 아이디 값에 @가 없으면 경고창 표시
  if(idValue.indexOf("@")==-1){
    alert("아이디는 이메일 형식으로 입력해 주세요"); 
    idEl.value();
    return;
  }
  //5. 폼 전송
  this.submit();
})