import sys
import socket
import string
import os

class ircbot:
	sock = None;

	info = {
		# connection info

		"ip": 	 	"irc.quakenet.org",
		"port":	 	6667,

		# bot info

		"nick":		"kitty___",
		"ident":	"kitty____",
		"realname": "kitty____",

		# irc info

		"owner":	"kaiske",
		"channel":	"csgo.na"
	};

	def connect( self ):
		self.sock = socket.socket();
		self.sock.connect( ( self.info[ "ip" ], self.info[ "port" ] ) );

	def login( self ):
		self.sock.send( "NICK " + self.info[ "nick" ] + "n" );
		self.sock.send( "USER " + self.info[ "ident" ] + " " + self.info[ "ip" ] + " bla :" + self.info[ "realname" ] + "n" );

	def receive( self ):
		line = self.sock.recv( 500 );
		line.rstrip();

		print( line );

		return( line );


if( __name__ == "__main__" ):
	bot = ircbot();

	bot.connect();
	bot.login();

	while( 1 ):
		bot.receive();
