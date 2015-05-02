import sys
import socket
import string
import os

class ircbot:
	sock = None;
	data = '';
	done = False;
	joindone = False;
	toquit = False;

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

	def cmd_quit( self, args ):
		self.sock.send( "QUIT :cufish\r\n" );
		self.toquit = True;

	commands = {
		":.quit": cmd_quit,
	};

	def parsecommand( self, text, command, offset = 1 ):
		parse_list = text.split( );
		loop = 0;

		for value in parse_list:
			print value;
			if( value == command ):
				return( parse_list[ loop + offset ] );
				break;
			loop = ( loop + 1 );

		return( None );

	def main( self ):
		if( self.data.find( "PING" ) != -1 ):
			if( self.parsecommand( self.data, "PING" ) != None ):
				#print( self.parsecommand( self.data, "PING" ) );
				self.sock.send( "PONG " + self.parsecommand( self.data, "PING" ) + "\r\n" );
			self.done = True;

		if( self.done == True ):
			self.sock.send( "USER " + self.info[ "nick" ] + " botxxx bot__ botxxx botxxx: Python IRC\r\n" );
			self.sock.send( "PASS " + self.info[ "password" ] + "\r\n" );
			self.sock.send( "JOIN " + self.info[ "channel" ] + "\r\n" );
			self.done = False;

		if( self.data.find( "/NAMES list." ) != -1 ):
			self.joindone = True;

		if( self.joindone == True ):
			#print( "PRIVMSG Q@CServe.quakenet.org :AUTH " + self.info[ "nick" ] + " " + self.info[ "password" ] + "\r\n" );
			self.sock.send( "PRIVMSG Q@CServe.quakenet.org :AUTH " + self.info[ "nick" ] + " " + self.info[ "password" ] + "\r\n" );
			self.joindone = False;

		for key, value in self.commands.iteritems():
			if( self.parsecommand( self.data, "PRIVMSG", 2 ) != None ):
				if( self.commands.has_key( self.parsecommand( self.data, "PRIVMSG", 2 ) ) ):
					args = "";
					self.commands[ self.parsecommand( self.data, "PRIVMSG", 2 ) ]( self, args );

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

		if( bot.toquit == True ):
			break;
