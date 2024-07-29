# Genomic Data Science Specialization - John Hopkins University (via Coursera) 
View the certification here: https://www.coursera.org/specializations/genomic-data-science 
- completed 24 total modules over 6 courses

<details>
<summary><strong> Course 1: Introduction to Genomic Technologies</strong></summary>
  
- completed 4 modules, 4 assessments, 1 course project
- revised fundamental genomics concepts and learned about next-generation sequencing techniques.
</details>

<details>
<summary><strong> Course 2: Python for Genomic Data Science</strong></summary>
<br>
<p> Completed 4 modules, 8 assessments, 1 course project. </p>

<details>
<br>
<summary><strong>Modules</strong></summary>

**Module 1 & 2:** Reviewed fundamental Python concepts, string manipulation

**Module 3:** Reading in & writing to files, manipulating FASTA and FASTQ files

**Module 4:**
- Using the `os` module for file & directory navigation
- Using the `sys` module to manipulate Python environment variables
- Using the `getopt` module to create command line programs
- Using the `subprocess` module to run command line tool pipelines with Python scripts
- Created my own modules & packages

</details>

<details>
<summary><strong>Course Project</strong></summary>
<br>

For the course project, I read in a multi-FASTA file and answered the following questions:

1. Number of sequences
2. Length of the longest and shortest sequences and their identifiers
3. Given a reading frame (1, 2, 3), find all open reading frames in that reading frame. Report the length of the longest ORF and its identifier.
4. Find the longest ORF in a given sequence and its index in that sequence

</details>
</details>

<details>
<summary><strong> Course 3: Algorithms for Genomic Data Science</strong></summary>
<br>
<p> Completed 4 modules, 4 projects </p>

<details>
<br>
<summary><strong>Modules</strong></summary>

**Module 1:** Reviewed functions / modules. 

**Module 2: Hamming Distance / Approximate Matching** 
- Learned online & offline algorithms to solve the read alignment problem: Boyer-Moore, variations of indexing (k-mer, subsequences).
- Utilized the pigeonhole principle to implement Boyer-Moore-assisted and indexing-assisted approximate matching algorithms. These algorithms align reads to segments in the genome that are a specified hamming distance away from a perfect match. 

**Module 3: Dynamic Programming** 
- Utilized dynamic programming approaches to
  - calculate edit distance
  - implement approximate matching algorithms that take substitutions **and** frameshift mutations into account.
  - implemented algorithms for global and local alignment.
  - build overlap graphs for genome assembly. 

**Module 4:**
- Learned how to find the shortest common superstring between multiple reads (for genome assembly) with two algorithms:
  - shortest common superstring: always accurate, not very efficient
  - greedy shortest common superstring: not always accurate, but more efficient. Uses the overlap map developed in module 3.
- Implemented DeBrujin graphs / Eulerian walks for assembly. 

</details>

<details>
<summary><strong>Course Projects</strong></summary>
<br>

**Project 1: Coliphage Genome Read Alignment** 
- Implemented / utilized exact matching algorithms to align reads to a Coliphage genome. - Assessed read quality of the Coliphage genome by position.

**Project 2: Approximate Matching Reads to Human Genome**
- Used Boyer-Moore-assisted and indexing-assisted approximate matching algorithms to align reads to hg38 (human genome).
- Counted number of comparisions (between reads and genome) made by various algorithms to compare their efficiences.
- Counted number of index hits made in k-mer index and subsequence index algorithms to compare efficiency.

**Project 3: Dynamic Programming**
- Implemented dynamic programming approximate matching algorithms
- Built an overlap map for a virus genome

**Project 4: Assembling a Virus Genome**
- Assembled a virus genome using the greedy shortest common superstring algorithm. 

</details>
</details>

<details>
<summary><strong> Course 4: Command Line Tools for Genomic Data Science</strong></summary>
<br>
<p> Completed 4 modules, 4 assessments, 4 course projects </p>

<details>
<br>
<summary><strong>Modules</strong></summary>

**Module 1:** 

**Module 2: Hamming Distance / Approximate Matching** 

**Module 3: Dynamic Programming** 

**Module 4:**


</details>

<details>
<summary><strong>Course Projects</strong></summary>
<br>

**Project 1: Coliphage Genome Read Alignment** 
- Implemented / utilized exact matching algorithms to align reads to a Coliphage genome. - Assessed read quality of the Coliphage genome by position.

**Project 2: Approximate Matching Reads to Human Genome**
- Used Boyer-Moore-assisted and indexing-assisted approximate matching algorithms to align reads to hg38 (human genome).
- Counted number of comparisions (between reads and genome) made by various algorithms to compare their efficiences.
- Counted number of index hits made in k-mer index and subsequence index algorithms to compare efficiency.

**Project 3: Dynamic Programming**
- Implemented dynamic programming approximate matching algorithms
- Built an overlap map for a virus genome

**Project 4: Assembling a Virus Genome**
- Assembled a virus genome using the greedy shortest common superstring algorithm. 

</details>
</details>

<details>
<summary><strong> Course 4: Command Line Tools for Genomic Data Science</strong></summary>
<br>
<p> Completed 4 modules, 4 assessments, 4 course projects </p>

Familiarized myself with following file formats: 
<br>
FASTA, FASTQ, BED, GFF3, GTF, SAM//BAM, VCF/BCF

Learned the following command line tools: 
<br>
Genome Alignment: bowtie2, BWA
<br>
SAM/BAM/VCF Manipulation: samtools, bedtools, BCFtools, igvtools. 
<br>
RNA-Seq analysis: tophat, cufflinks, cuffdiff 

Completed 4 projects using these tools to extract information out of various file formats. For more detail, see the course folder. 

</details>

<details>
<summary><strong> Course 5: Biocondctor for Genomic Data Science and Course 6: Statistics for Genomic Data Science </strong></summary>
<br>
<p> Completed 8 modules, 8 course projects </p>

Course 5: 
- Learned common data structures: ExpressionSets, SummarizedExperiment and GRanges used across several types of analyses.
- Learned how to represented and compute on genomes.
- Covered data structures and R S4 Classes: how to navigate R classes and get documentation / help.
- Learned how to access data from online databases through bioconductor packages.

Course 6: 
(Descriptions lifted from: https://www.coursera.org/learn/statistical-genomics?specialization=genomic-data-science)
- core statistics ideas: normalization, exploratory analysis, linear modeling, testing, and multiple testing
- preprocessing, linear modeling, and batch effects
- modeling non-continuous outcomes (like binary or count data), hypothesis testing, and multiple hypothesis testing
- general pipelines people use to analyze specific data types like RNA-seq, GWAS, ChIP-Seq, and DNA Methylation studies

Bioconductor Packages I learned in these two courses: 

Annotation / Interfacing with Browsers: AnnotationHub, biomaRt, GEOQuery, ArrayExpress, GenomicFeatures, rtracklayer, SRAdb.
<br>
Genomic Data Structures: GenomicRanges, Biostrings, BSgenome, Views, Rle (Run length encoding), ShortRead, RSamtools, broom.
<br>
Data Preprocessing: preprocessCore, BioBase 
<br>
Data Analysis & Visualization: oligo, DESeq2, limma, edgeR, snpStats, goseq
<br>
Modeling: lm, glm
<br>

</details>
