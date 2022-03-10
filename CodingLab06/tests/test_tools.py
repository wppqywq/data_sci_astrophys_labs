import unittest
import nose.tools as nt
import numpy as np
import tools


class test_tools():

    def setUp(self):
        # Create a random array
        self.n = 4
        self.rand_array = np.random.normal(size=(self.n,self.n))
        # use my test data
        self.data = "test_data.dat"
        self.delimiter = ' '

    def tearDown(self):
        pass

    def test_square(self):
        print(self.rand_array)

        # Test the square function to see if it
        # returns an array of the right size
        output_arr = tools.square(self.rand_array)
        nt.assert_equal(output_arr.shape, (self.n, self.n))

        # Test the square function to make sure that squaring
        # a matrix containing only 1s and 0s returns the same thing
        test_arr = np.diag(np.ones(self.n))
        output_arr = tools.square(test_arr)
        for i in range(self.n):
            for j in range(self.n):
                nt.assert_equal(output_arr[i,j], test_arr[i,j])

        # Test the square function for a known input/output
        test_arr = np.array([1, 2])
        output_arr = tools.square(test_arr)
        nt.assert_equal(output_arr[0], 1)
        nt.assert_equal(output_arr[1], 4)


    def test_get_pi(self):
        # See if the get_pi function really returns pi
        alleged_pi = tools.get_pi()
        nt.assert_almost_equal(alleged_pi, 3.141592653589)

    def test_picky(self):
        # Make sure that tools.picky raises an error if the
        # wrong type is inputted
        nt.assert_raises(TypeError, tools.picky, 'hey')

    def test_read_df_1(self):
        # to check the size
        file_length = len(open(self.data).readlines())
        out_put = tools.read_df(self.data, delimiter=self.delimiter)

        nt.assert_equal(out_put.shape[0], file_length)

    def test_read_df_2(self):
        # to check the delimiter and if the data is correct
        output_line0 = tools.read_df(self.data, delimiter=self.delimiter).iloc[0]
        line0 = open(self.data).readline().split(self.delimiter)

        nt.assert_equal(output_line0['day'], (float(line0[0])-1973)*366.242)
        nt.assert_equal(output_line0[1], float(line0[1]))
        nt.assert_equal(output_line0[2], float(line0[2]))



