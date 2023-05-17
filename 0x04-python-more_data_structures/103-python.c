#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	PyBytesObject *bytes;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);
	printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)bytes->ob_sval[i]);
		if (i == 9)
			break;
		printf(" ");
	}

	printf("\n");
}
