import pandas as pd
import os
import sys
import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter
from fpdf import FPDF
import time

TEMP_DIR = "pdf_temp"


def generate_dataframe_summary(df, dataset_name):
    pdf = FPDF()
    pdf.set_font("Arial", size = 20)

    # Add a page
    pdf.add_page()
    line_number = 1

    # ADD TITLE
    if dataset_name.lower() == "booking":
        pdf.cell(200, 10, txt="BOOKING.COM EXPLORATION SUMMARY", ln=line_number, align='C')
    elif dataset_name.lower() == "twitter":
        pdf.cell(200, 10, txt="TWITTER EXPLORATION SUMMARY", ln=line_number, align='C')
    else:
        raise ValueError("Unknown Dataset") 
    line_number += 1

    # Add Feature Counts
    pdf.set_font("Arial", size = 12)
    pdf, line_number = pdf_feature_counts(df, dataset_name, pdf, line_number)
    
    # Add Trip Type Summary
    if "trip_type" in df.columns:
        original_stdout = sys.stdout # Save a reference to the original standard output
        
        with open('filename.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print("#######################################")
            print("Single-City Trips")
            print(df["trip_type"].value_counts()/len(df)*100)
            x = df[df["trip_type"] == "Domestic"].groupby(["user_id"])["trip_duration"].mean().values
            params = "Domestic - Mean: " + str(x.mean().round(3)) + ", Std:" + str(x.std().round(3))
            print(params)
            x = df[df["trip_type"] == "International"].groupby(["user_id"])["trip_duration"].mean().values
            params = "International - Mean: " + str(x.mean().round(3)) + ", Std:" + str(x.std().round(3))
            print(params)
            print("#######################################")
            print("Multi-City Trips")
            print(df.drop_duplicates("utrip_id")["trip_type"].value_counts()/len(df.drop_duplicates("utrip_id"))*100)
            x = df[df["trip_type"] == "Domestic"].groupby(["user_id", "utrip_id"])["trip_duration"].sum().values
            params = "Domestic - Mean: " + str(x.mean().round(3)) + ", Std:" + str(x.std().round(3))
            print(params)
            x = df[df["trip_type"] == "International"].groupby(["user_id", "utrip_id"])["trip_duration"].sum().values
            params = "International - Mean: " + str(x.mean().round(3)) + ", Std:" + str(x.std().round(3))
            print(params)
            sys.stdout = original_stdout # Reset the standard output to its original value

        # Add output in PDF
        pdf.add_page()
        f = open('filename.txt', "r")
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='L')
    
    pdf.output("pdf_temp/00_summary.pdf")


def get_pdfs_path():
    files = os.listdir(TEMP_DIR)

    files_pdf = [i for i in files if i.endswith('.pdf')]
    files_pdf = sorted(files_pdf)
    return files_pdf


def merge_pdfs(output):
    paths = get_pdfs_path()
    
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(TEMP_DIR + "/" + path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)
        

def save_plot(plt_):
    time.sleep(1)
    fout = TEMP_DIR + "/" + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".pdf"
    plt_.savefig(fout, bbox_inches='tight')
    

def delete_directory():
    for file in os.scandir(TEMP_DIR):
        if file.name.endswith(".pdf"):
            os.unlink(file.path)
    os.rmdir(TEMP_DIR)
    

def create_directory():
    if os.path.exists(TEMP_DIR):
        delete_directory()
    os.mkdir(TEMP_DIR)
