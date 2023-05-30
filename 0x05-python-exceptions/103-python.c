#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))  // Check if the object is of type list
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	int listSize, allocation, i;
	const char *elementType;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	listSize = var->ob_size;
	allocation = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", listSize);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < listSize; i++)
	{
		elementType = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, elementType);
		if (strcmp(elementType, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(elementType, "float") == 0) // Print float objects
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))  // Check if the object is of type bytes
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *str = PyBytes_AsString(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size < 0 || size > 10) size = 10;
	printf("  first %ld bytes:", size);
	for (int i = 0; i < size; i++) {
		printf(" %02hhx", str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - prints some basic info about Python float objects
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p)) // Check if the object is of type float
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);
	printf("[.] float object info\n");
	printf("  value: %g\n", value);
}
