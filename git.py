
""" 
Git 명령어 & Tips 

작업공간 -> add -> staging area -> commit -> repository(저장소) 

1. 저장을 위한 도구로서의 Git

commit : 저장소의 check point (저장 분기점)
어떤 변경사항들이 저장되었는지 기록 (수틀리면 되돌아가기 쉬움)


$ git init : Git 저장소 초기화 (프로젝트 초기에 한 번만)

$ git status : 저장소 상태 체크 , 현재 프로젝트 변경사항 확인

$ git add. ($ git add -A) : 모든 파일을 staging area로 올리기 (특정 파일을 add : $ git add <filename>)

$ git commit -m <설명> : 저장소로 commit 하기


로컬 repository -> 온라인 repository

$ git remote add origin <github 주소>

$ git push (-u origin master) 


gitignore : Git 에 올리고 싶지 않은 것들을 미리 걸러 놓음



2. 협업을 위한 도구로서의 Git





"""