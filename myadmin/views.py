# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from .models import ProductModel,ProductListing,ProductVariant,Brand,Category,Store
from .forms import UploadDataForm
import csv
import codecs

def update_price(request):

    products = ProductListing.objects.all()
    return render(request, 'pricehound_admin/product_list.html', {'products':products})


def Upload_Data(request):

    if request.method == "POST":
        Mydataupload=UploadDataForm(request.POST,request.FILES)

        if Mydataupload.is_valid():
            csvfile = request.FILES['File']
            datatoupload=request.POST.get('Option')
            dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
            csvfile.open()
            data = csv.reader(codecs.EncodedFile(csvfile, "utf-8"))
            
            if (datatoupload=="Models"):
                try:
                    first_frame=1
                    for row in data:
                        if(first_frame==1):
                            first_frame=0
                            continue

                        Primary_Key_Brand= Brand.objects.get(name=row[0])
                        Primary_Key_Category=Category.objects.get(name=row[2])
                        product_exist= ProductModel.objects.all()

                        if (ProductModel.objects.filter(brand=Primary_Key_Brand,name=row[1]).exists()):
                            continue
                        else:
                            product= ProductModel(brand=Primary_Key_Brand,name=row[1],category=Primary_Key_Category)
                            product.save()
                            print product

                except (IOError):
                    print 'Variant CSV File is not found the directory'

            elif (datatoupload=="Variants"):
                try:
                    first_frame=1
                    for row in data:
                        if(first_frame==1):
                            first_frame=0
                            continue

                        Primary_Key_Model= ProductModel.objects.all()

                        for products in Primary_Key_Model:
                            if(str(products)==row[0]):
                                if (ProductVariant.objects.filter(product_model=products,color=row[1],capacity=row[2]).exists()):
                                    continue
                                else:
                                    product= ProductVariant(product_model=products,color=row[1],capacity=row[2])
                                    product.save()
                                    print product

                except (IOError):
                    print 'Variant CSV File is not found the directory'

            elif (datatoupload=="Listings"):
                try:
                    first_frame=1
                    for row in data:
                        if(first_frame==1):
                            first_frame=0
                            continue

                        Primary_Key_Variant= ProductVariant.objects.all()

                        for products in Primary_Key_Variant:
                            if(str(products)==row[0]):
                                Primary_Key_Store=Store.objects.get(name=row[1])
                                if ProductListing.objects.filter(product_variant=products,store=Primary_Key_Store,product_id=row[2]).exists():
                                    continue
                                else:
                                    product= ProductListing(product_variant=products,store=Primary_Key_Store,product_id=row[2])
                                    product.save()
                                    print product
                except (IOError):
                    print 'Listing CSV File is not found the directory'

            return HttpResponse("All data's are uploaded successfully..")

    else:
        uploadform=UploadDataForm()

    print "Data store "
    return render(request, 'DataManager/DataUpload.html',{'uploadform':uploadform})
