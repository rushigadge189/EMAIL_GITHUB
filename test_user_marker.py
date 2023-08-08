import pytest

class Test_User_Marker() :

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_cust ( self ) :
        print ( 'Customer Added Successfully') ;

    @pytest.mark.regression
    def test_delete_cust ( self ) :
        print ('Customer Deleted Successfully') ;

    @pytest.mark.regression
    def test_update_cust ( self ) :
        print ( 'Customer Updated Successfully' ) ;

    @pytest.mark.sanity
    def test_add_prod ( self ) :
        print ( 'Product Added Successfully' ) ;

    @pytest.mark.sanity
    def test_delete_prod ( self ) :
        print ( 'Product Deleted Successfully' ) ;

    @pytest.mark.sanity
    def test_update_prod ( self ) :
        print ( 'Product Updated Successfully' ) ;

    @pytest.mark.adhoc
    def test_bill_gen ( self ) :
        print ( 'Bill Generated Successfully' ) ;

    @pytest.mark.adhoc
    def test_bill_update(self):
        print ( 'Bill Updated successfully' ) ;

    @pytest.mark.adhoc
    def test_bill_del(self):
        print ( 'Bill Deleted Successfully' ) ;

