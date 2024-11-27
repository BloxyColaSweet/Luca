segment .data

segment .text
	global _start

; *** exit function is used to exit the program ***
exit:
	; *** set up the stack frame ***
	push rbp
	mov rbp, rsp

	mov rax, 60

	; quad parameter exit code
	mov rdi, rbp + 16
	syscall

	; *** unpacking the stack frame ***
	mov rsp, rbp
	add rbp, 8
	pop rbp

	; clear parameters by n times
	pop r15
	times 1 pop r14
	push r15

	; return
	ret

; *** alloc function is used to allocate a memory region ***
alloc:
	; *** set up the stack frame ***
	push rbp
	mov rbp, rsp

	mov rax, 9
	xor rdi, rdi

	; quad parameter allocation size
	mov rsi, rbp + 16

	; quad parameter protocol
	mov rdx, rbp + 24 

	; quad parameter flags
	mov r10, rbp + 32

	; no fd and offset
	xor r9, r9
	xor r8, r8

	syscall

	; *** unpacking the stack frame ***
	mov rsp, rbp
	add rbp, 8
	pop rbp

	; clear parameters by n times
	pop r15
	times 3 pop r14
	push r15

	; return
	ret

; *** main process ***
_start:
	; *** set up the stack frame ***
	push rbp
	mov rbp, rsp
	
	; *** calling alloc ***

	; move last parameter for function alloc for parameter flags: 22
	mov rax, 22
	push rax

	; move parameter for function alloc for parameter protocol: 3
	mov rax, 3
	push rax

	; move first parameter for function alloc for parameter allocation size: 1
	mov rax, 1
	push rax

	; call the function alloc
	call alloc


	; *** calling exit ***

	; move first parameter for function exit for parameter exit code: 0
	mov rax, 0
	push rax

	; call the function exit
	call exit


	; *** unpacking the stack frame ***
	mov rsp, rbp
	add rbp, 8
	pop rbp

	; clear parameters by n times
	pop r15
	times 0 pop r14
	push r15

	; return
	ret
