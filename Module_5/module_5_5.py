# Классы и объекты. Практика

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        return other.title == self.title


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname

    def get_info(self):
        return self.nickname, hash(self.password)  # тут hash добавил так как при проверке в log_in сравнивается с hash


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname, hash(password)) == user.get_info():
                self.current_user = user
                return
            ''' 
            тут не совсем понял зачем применять метод get_info(), когда можно написать
            if (nickname, hash(password)) == (user.nickname, hash(user.password)): 

            '''

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:  # ДЛЯ СЕБЯ - пригодился переопределенный eq чтобы при проверке наличия сравнивались nickname
            self.users.append(new_user)
            self.log_in(nickname, password)  # тут если не логиниться то не проверится метод log_in

        else:
            print(f'Пользователь {nickname} уже существует.')

    def add(self, *args: Video):
        for video in args:
            if video not in self.videos:  # ДЛЯ СЕБЯ - пригодился переопределенный eq чтобы при проверке наличия сравнивались title
                self.videos.append(video)

    def get_videos(self, word):
        founded_videos = []
        for video in self.videos:
            if word.lower() in str(video).lower():
                # str(video) возвращает нам title, смысл тут применять метод, если in video.title.lower() можно написать?
                founded_videos.append(video)
        return founded_videos

    def watch_video(self, video_title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if video_title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                    video.time_now = 0
                    print('Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                break


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)  # чтобы проверить условие добавления видео

ur.add(v1, v2, v3)
print()
print(ur.videos)

print()
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
