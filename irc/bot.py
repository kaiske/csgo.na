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

		"nick":		"friend",
		"realname": "GATHERBOT",

		# irc info

		"owner":	"kaiske",
		"channel":	"#csgo.na",
		"password":	"hellox86"
	};

	def connect( self ):
		self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM );
		self.sock.connect( ( self.info[ "ip" ], self.info[ "port" ] ) );

	def login( self ):
		self.sock.send( "NICK " + self.info[ "nick" ] + "\r\n" );
		self.sock.send( "USER " + self.info[ "nick" ] + " 8 * :" + self.info[ "realname" ] +"\r\n" );
		self.sock.send( "PASSWORD " + self.info[ "password" ] + "\r\n" );
		self.sock.send( "JOIN " + self.info[ "channel" ] + "\r\n" );

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
