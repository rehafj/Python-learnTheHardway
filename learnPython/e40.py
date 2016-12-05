class mystuff(object):
	def __init__(self):
		self.tangariene = " ad now a 1000 years in between"

	def apple(self):
		print" i am a classy apple"
	
	
var = mystuff()
var.apple()
print var.tangariene 


#dic style

mydic= {"key1":"item1", "key2":"item2"}
print mydic["key2"]

#module style 
import ex 
ex.apple()
print ex.tan


# class style 
var = mystuff()
x = var.tangariene
print x 
var.apple()


class song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
		self.num = 10
	def sing_me_a_song(self):
		print " ***" * 10 
		for line in self.lyrics:
			print line
		print " ***" * 10 
		
	def bash_and_trash(self, var):
		
		return self.num * var 
	
happy_bday = song([" happy birthday to you",
					" you smell like my shoe",
						"and ypu look like a monkey too!"])
						
var2 = song([" happy unbirthday to me",
					" to me? too yu!",
						"happy happy unbirthdaaaaay to youuuuuu"])
						
newsong = [" this is my song to you!"]


happy_bday.sing_me_a_song()
x = happy_bday.bash_and_trash(9)
print x
happy_bday = song(newsong)
happy_bday.sing_me_a_song()

var2.sing_me_a_song()


