import os, csv
from post import Post
#파일 경로
file_path = "./myvenv/Chapter12/data.csv"

#post 객체를 저장할 리스트
post_list = []
if os.path.exists(file_path):
  #게시글 로딩
  print('loading...')
  f = open(file_path, 'r', encoding= 'utf-8')
  reader = csv.reader(f)
  for data in reader:
    post = Post(int(data[0]), data[1], data[2], int(data[3]))
    post_list.append(post)

else:
  #파일이 존재하지 않을 시 생성
  f = open(file_path, 'w', encoding='utf-8', newline='')
  f.close()

def write_post():
  """게시글 쓰기 함수"""
  print('\n\n 게시글 쓰기 -')
  title = input('제목을 입력하여주세요\n>>>')
  content = input('내용을 입력하여주세요\n>>>')
  #글 번호
  id = post_list[-1].get_id() + 1
  post = Post(id, title, content, 0)
  post_list.append(post)
  print('#게시글이 등록되었습니다.')

def list_post():
  id_list= []
  '''게시글 목록 함수'''
  print('\n\n- 게시글 목록 -')
  for post in post_list:
    print('번호:',post.get_id())
    print('제목:',post.get_title())
    print('조회수:',post.get_view_count())
    print('\n')
    id_list.append(post.get_id())
  
  while True:
    print('Q) 글 번호를 입력해주세요.(종료: -1)')
    try:
      id = int(input('>>>'))
      if id in id_list:
        print('게시글 상세보기')
        detail_post(id)
        break
      elif id == -1:
        break
      else:
        print('없는 번호 입니다.')
    except ValueError:
      print('숫자를 입력해주세요')

def update_post(target_post):
  '''게시글 수정 함수'''
  print('\n\n- 게시글 수정 -')
  title = input('제목을 입력해주세요. \n>>>')
  content = input('본문을 입력해주세요. \n>>>')
  target_post.set_post(target_post.id, title, content, target_post.view_count)
  print('게시글이 수정되었습니다.')

def delete_post(target_post):
  post_list.remove(target_post)
  print('게시글이 삭제되었습니다.')

def save():
  f = open(file_path, 'w',encoding='utf-8', newline='')
  writer = csv.writer(f)
  for post in post_list:
    row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
    writer.writerow(row)
  f.close()
  print('저장완료')
  print('프로그램 종료')

#글 상세보기
def detail_post(id):
  '''게시글 상세보기 함수'''
  print('\n\n - 게시글 상세 -')
  for post in post_list:
    if post.get_id() == id:
      #조회수 1 증가
      post.add_view_count()
      print('번호:', post.get_id())
      print('제목:', post.get_title())
      print('본문:', post.get_content())
      print('조회수:', post.get_view_count())
      target_post = post
  while True:
    print('Q) 수정: 1, 삭제: 2 (메뉴: -1)')
    try:
      choice = int(input('>>>'))
      if choice == 1:
        update_post(target_post)
        break
      elif choice == 2:
        delete_post(target_post)
        break
      elif choice == -1:
        break
      else:
        print('잘못 입력하셨습니다.')
    except ValueError:
      print('숫자를 입력해 주세요.')
#메뉴 출력하기
while True:
  print('\n\n FASTCAMPUS BLOG -')
  print('-메뉴를 출력해주세요 -')
  print('1. 게시글 쓰기')
  print('2. 게시글 목록')
  print('3. 프로그램 종료')
  try:
    choice = int(input('>>>'))
  except ValueError:
    print('숫자를 입력해 주세요.')
  else:
    if choice == 1:
      write_post()
    elif choice == 2:
      list_post()
    elif choice == 3:
      save()
      break 