import sys
import socket
import string
import os

class ircbot:
	sock = None;
	data = '';
	done = False;
	joindone = False;

	info = {
		# connection info

		"ip": 	 	"irc.quakenet.org",
		"port":	 	6667,

		# bot info

		"nick":		"friend",
		"realname": "GATHERBOT.NA",

		# irc info

		"owner":	"kaiske",
		"channel":	"#csgo.na",
		"password":	"hellox86"
	};

	def main( self ):
		if( self.data.find( "PING" ) != -1 ):
			splits = self.data.split();
			loopnum = 0;

			for value in splits:
				if( value == "PING" ):
					print( splits[ loopnum + 1 ] );
					self.sock.send( "PONG " + splits[ loopnum + 1 ] + "\r\n" );
					break;

				loopnum = loopnum + 1;

			self.done = True;

		if( self.done == True ):
			self.sock.send( "USER " + self.info[ "nick" ] + " botxxx bot__ botxxx botxxx: Python IRC\r\n" );
			self.sock.send( "PASS " + self.info[ "password" ] + "\r\n" );
			self.sock.send( "JOIN " + self.info[ "channel" ] + "\r\n" );
			self.done = False;

		if( self.data.find( "/NAMES list." ) != -1 ):
			self.joindone = True;

		if( self.joindone == True ):
			print( "PRIVMSG Q@CServe.quakenet.org :AUTH " + self.info[ "nick" ] + " " + self.info[ "password" ] + "\r\n" );
			self.sock.send( "PRIVMSG Q@CServe.quakenet.org :AUTH " + self.info[ "nick" ] + " " + self.info[ "password" ] + "\r\n" );
			self.joindone = False;

		print( self.data );

	def connect( self ):
		self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM );
		self.sock.connect( ( self.info[ "ip" ], self.info[ "port" ] ) );

	def login( self ):
		self.sock.send( "NICK " + self.info[ "nick" ] + "\r\n" );
		#self.sock.send( "USER " + self.info[ "nick" ] + " botxxx bot__ botxxx botxxx: Python IRC\r\n" );
		#self.sock.send( "PASS " + self.info[ "password" ] + "\r\n" );
		#self.sock.send( "JOIN " + self.info[ "channel" ] + "\r\n" );

	def receive( self ):
		self.data = self.sock.recv( 4096 );
		self.main();

if( __name__ == "__main__" ):
	bot = ircbot();

	bot.connect();
	bot.login();

	#bot.data = bot.sock.recv( 4096 );

	while( 1 ):
		bot.receive();
