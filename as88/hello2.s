! Simple 'hello world' program
! See section 9.8.1.

	_EXIT	= 1		!  1
	_WRITE	= 4		!  2
	_STDOUT	= 1		!  3
.SECT .TEXT             ! begin the code segment (.TEXT)
start:                  ! optional label for first instr
MOV	CX, b-a
PUSH    CX              ! perform _WRITE:  push arg3
PUSH    a              !    push arg2
PUSH    _STDOUT         !    push arg1
PUSH    _WRITE          !    push system-call number
SYS                     !    perform system call
ADD SP,8                !    clean up the stack
MOV     CX,b-a     ! move length of string to CX
PUSH    CX              ! perform _WRITE:  push arg3
PUSH    b              !    push arg2
PUSH    _STDOUT         !    push arg1
PUSH    _WRITE          !    push system-call number
SYS                     !    perform system call
ADD     SP,8            !    clean up the stack
SUB CX,AX               ! subtract return value from len
PUSH    CX              ! perform _EXIT:  push arg1
PUSH    _EXIT           !    push system-call number
SYS                     !    perform system call
.SECT .DATA			! 17
a:
.ASCII	"Hello\n"
b:
.ASCII "Goodbye\n"
endb:	.BYTE	0
.SECT .BSS