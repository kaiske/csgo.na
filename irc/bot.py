import sys
import socket
import string
import os

class ircbot:
	sock = None;

	info = {
		# connection info

		"ip": 	 	"ip_here",
		"port":	 	6667,

		# bot info

		"nick":		"bot_name_un9k",
		"ident":	"bot_name",
		"realname": "bot_name",

		# irc info

		"owner":	"owner_name",
		"channel":	"default_channel"
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
