def get_sample_news():
    return [
        {
            'title': 'Red Hat to maintain OpenJDK 8 and OpenJDK 11',
            'text': """Red Hat is taking over maintenance responsibilities for OpenJDK 8 and OpenJDK 11 from Oracle. 
            Red Hat will now oversee bug fixes and security patches for the two older releases, which serve as the 
            basis for two long-term support releases of Java. 

Red Hat’s updates will feed into releases of Java from Oracle, Red Hat, and other providers. Oracle released JDK (
Java Development Kit) 8, based on OpenJDK 8, in March 2014 while JDK 11, based on OpenJDK 11, arrived in September 
2018. Previously, Red Hat led the OpenJDK 6 and OpenJDK 7 projects. Red Hat is not taking over OpenJDK 9 or OpenJDK 
10, which were short-term releases with a six-month support window. 

[ 15 Java frameworks that give developers a boost. • Which tools support Java’s new modularity features. | Keep up 
with hot topics in programming with InfoWorld’s App Dev Report newsletter. ] Users should not expect any radical 
additions to OpenJDK 8 or OpenJDK 11, as new or experimental features only go into the latest version of standard 
Java. The current version of standard Java, JDK 12, was released last month. The next version, which will be based on 
OpenJDK 13, is expected to be completed in September, with Oracle set to release JDK 13. 

Red Hat in December announced commercial support for OpenJDK on Windows. The company’s Java plans also include 
launching OpenJDK in a Microsoft installer in coming weeks and distributing IcedTea-Web, a free software 
implementation of the Java Web Start tool for running Java applications from the web. IcedTea Web will be part of the 
Windows OpenJDK distribution. 

This story, "Red Hat to maintain OpenJDK 8 and OpenJDK 11" was originally published by InfoWorld.""",
            'date': '2019-04-18',
            'views': 0,
            'image_url': 'https://images.idgesg.net/images/article/2018/07'
                         '/time_clock_history_coffee_java_by_matthew_kerslake_cc0_via_unsplash_1200x800-100765108'
                         '-large.jpg',
            'category_fk': 2
        },
        {
            'title': 'Google Cloud Run runs stateless containers, serverlessly',
            'text': """Google has expanded its serverless compute options with the addition of Cloud Run, a managed 
            compute service that lets you run stateless containers that are invocable via HTTP requests. Cloud Run is 
            also available on Google Kubernetes Engine (GKE), allowing you to run containerized HTTP workloads on a 
            managed Kubernetes cluster. 

Cloud Run lets developers take advantage of the portability of containers and the velocity of serverless computing. 
Now in beta, Cloud Run provides for automated provisioning and scaling of workloads, with users paying only for the 
resources their containers actually use. On GKE, Cloud Run allows stateless HTTP workloads to run on existing 
Kubernetes clusters, with users having access to custom machine types, Google Compute Engine networks, 
and the ability to run side-by-side with other workloads in the same cluster. 

[ What is Docker? Linux containers explained. | Dig into the the red-hot open source framework in InfoWorld’s 
beginner’s guide to Docker. | Check out our Docker tutorials: Get started with Docker. • Get started with Docker 
swarm mode. • Get started with Docker Compose. • Get started with Docker volumes. • Get started with Docker 
networking. ] Cloud Run allows developers to build applications in any language, using the tools and dependencies of 
their choice. Cloud Run is based on Knative, an open API and software layer that lets users move “serverless” 
workloads across Kubernetes platforms including Google Cloud Platform, GKE, and anywhere else that Kubernetes runs. 

Key features of Cloud Run include:

A command line and user interface for deploying and managing services. Autoscaling, moving up and down from zero to N 
based on traffic. When running on GKE, autoscaling is limited to the capacity within the cluster. Users can select 
their own language or operating system libraries as well as use their own binaries. Container workflows and standards 
can be leveraged. Cloud Run can be paired with Cloud Build, Container Registry, and Docker, among others. Redundancy 
is provided. Services are regional and automatically replicated across multiple zones. Integrated logging and 
monitoring, including Stackdriver monitoring, logging, and error-reporting. Users can map services to their own 
domains. Cloud Run shares core infrastructure with two other serverless technologies at Google, Google Cloud 
Functions and Google App Engine. You can go to the Google Cloud Platform website to start a free trial. 

This story, "Google Cloud Run runs stateless containers, serverlessly" was originally published by InfoWorld.""",
            'date': '2019-04-11',
            'views': 0,
            'image_url': 'https://images.idgesg.net/images/article/2018/07/google-cloud-services-100765812-large.jpg',
            'category_fk': 2
        },
        {
            'title': 'Alibaba offers its own Java distribution',
            'text': """Make room, Oracle, SAP, and other Java distributors. E-commerce vendor Alibaba now has its own 
            Java distribution too, the open source Dragonwell8 Java Development Kit (JDK). 

The beta Alibaba Dragonwell8 is based on OpenJDK and Java SE (Standard Edition) 8. It is similar to the Amazon 
Corretto Java build and the Azul Zulu Java platform. Currently, Allibaba only works with Intel x86-64 Linux systems, 
with a focus on stability and enhancements for large-scale Java applications in data centers. A Dragonwell release is 
planned for every quarter. Dragonwell 11, based on Java SE 11, is due by 2020. 

[ 15 Java frameworks that give developers a boost. • Which tools support Java’s new modularity features. | Keep up 
with hot topics in programming with InfoWorld’s App Dev Report newsletter. ] Dragonwell8's features include: 

CMS (-XX:+UseConcMarkSweep) serves as the default garbage collector. Java Flight Recorder, backported from JDK 11. 
Servicing capabilities, including the ArrayAllocationWarningSize option for printing the calling stack of an array 
allocation. JWarmup pre-compiliation. Like SAP’s SapMachine Java variant, Dragonwell is described by Alibaba as a 
“friendly fork,” offered under the same terms as OpenJDK. Dragonwell was derived from the Alibaba/Alipay JDK, 
which supports the company’s Taobao website, Ant Financial financial services, and Cainiao logistics. Alibaba is 
contributing technology developed for Dragonwell back to OpenJDK at large, including a preview of Java Flight 
Recorder and JWarmup. 

Where to download Dragonwell8
You can download Dragonwell8 from GitHub.

This story, "Alibaba offers its own Java distribution" was originally published by InfoWorld.""",
            'date': '2019-04-02',
            'views': 0,
            'image_url': 'https://images.techhive.com/images/article/2017/04/dragon_statue_head-100717539-large.jpg',
            'category_fk': 2
        },
        {
            'title': 'Java and JVM to zero in on GPUs and containers',
            'text': """The development of the Java programming language going forward will emphasize support for 
            modern computing platforms including GPUs and containers, Oracle revealed in a presentation on March 21. 
            Among other things, the company’s plans call for ensuring that Java provides strong support for GPUs and 
            hardware acceleration, which will be key to supporting machine learning and artificial intelligence 
            workloads. 

The Java SE (Standard Edition) development team at Oracle want to configure Java such that the JVM will understand 
which workloads should run on the GPU and which should run on the CPU. GPUs, while initially built for image 
processing, are increasingly being used for number-crunching applications, machine learning, and even databases. 

[ 15 Java frameworks that give developers a boost. • Which tools support Java’s new modularity features. | Keep up 
with hot topics in programming with InfoWorld’s App Dev Report newsletter. ] Oracle said that the JVM also needs to 
understand the resource constraints imposed by containers. Container-oriented optimizations will include performance 
enhancements as well as faster cold and warm startups. Other opportunities and goals cited for the development of 
Java include: 

Making Java as small as possible to reduce its footprint and run workloads with the smallest resource consumption and 
lowest cost. Scalability for big data, toward petabyte-sized heaps. Predictability at scale. Data density, 
with the presentation of data in the JVM as concise as possible. Native access, with the ability to access libraries 
in spaces such as artificial intelligence and machine learning. Making it easier and more efficient to get data in 
and out of the JVM. Developer productivity and continued language enhancements. Oracle drew attention to a number of 
innovative Java projects including Valhalla, an incubator project for virtual machine and language features; Panama, 
for accessing non-Java APIs; and Loom, to make it easier to handle concurrency in applications. 

Oracle also pointed to the gradual elimination of Java’s finalization capability, for performing postmortem cleanup 
on objects that the garbage collector found unreachable. Finalization has made garbage collection more expensive, 
with the collector having to perform an extra pass. There are now better ways to deal with the task, Oracle said, 
such as the java.lang.ref subsystem. 

Oracle has just released Java Development Kit 12, featuring a preview of switch expressions to simplify coding. Also 
in JDK 12 is an abortable mixed collections capability for the G1 garbage collector. JDK 13 is due in September. 
Features are still be determined, although raw string literals and a production version of switch expressions are 
expected. 

This story, "Java and JVM to zero in on GPUs and containers" was originally published by InfoWorld.""",
            'date': '2019-03-26',
            'views': 0,
            'image_url': 'https://images.idgesg.net/images/article/2018/07/coffee_beans_java_bliss_jolt_caffeine_by'
                         '-ryan-mcguire-gratisography-100764932-large.jpg',
            'category_fk': 2
        },
        {
            'title': 'Gluon ships JavaFX 12',
            'text': """Mobile solutions provider Gluon has released JavaFX 12, the company’s second release of the 
            rich client technology for Java since JavaFX was decoupled from the JDK (Java Development Kit). 

[ 15 Java frameworks that give developers a boost. • Which tools support Java’s new modularity features. | Keep up 
with hot topics in programming with InfoWorld’s App Dev Report newsletter. ] JavaFX 12 follows on Gluon’s September 
2018 release of JavaFX 11. The JavaFX 12 runtime is available as a platform-specific SDK, as JMOD archive files, 
and as a set of artifacts in the Maven Central repository. Key capabilities in JavaFX 12 include: 

New protected VirtualFlow methods for subclassing. Implementation of accelerated composition for WebView. The 
addition of an API in GraphicsContext to control image-smoothing. Reintroduction of the JFR (Java Flight Recorder) 
Pulse Logger. Refactoring of the javafx.swing implementation to remove an unneeded abstraction layer. Use of the 
xdg-open tool to get the default web browser on Linux systems. Support for mouse forward and back buttons. The JavaFX 
12 release also fixes a number of bugs, such as a blurry font issue on Ubuntu 16.04 and Debian 9, and slow mousewheel 
scrolling on MacOS X. JavaFX 12 will be supported for six months until the release of JavaFX 13. JavaFX 11 is the 
current long-term support release. 

JavaFX is a rich media technology founded by Sun Microsystems in May 2007. The project passed to Oracle when Oracle 
acquired Sun in 2010. Oracle a year ago decided to decouple JavaFX from the JDK to make it easier to adopt and 
attract new participants in its development. 

You can download JavaFX 12 from the Gluon JavaFX project website. JavaFX is licensed under the GPL v2 plus Classpath.

This story, "Gluon ships JavaFX 12" was originally published by InfoWorld.""",
            'date': '2019-03-21',
            'views': 0,
            'image_url': 'https://images.idgesg.net/images/article/2018/10/java_coffee_cup-of-coffee_mug_white'
                         '-saucer_froth-100777466-large.jpg',
            'category_fk': 2
        },
        {
            'title': 'Jenkins tries to reinvent itself as cloud-native for Kubernetes',
            'text': """The popular but troubled Jenkins CI/CD system is being reworked to support cloud-native 
            applications on the Kubernetes container-orchestration platform. The Jenkins X project is a response to 
            user concerns that Jenkins had lost its luster and had developed configuration and stability issues. 

Jenkins X is intended for Kubernetes users who want to adopt CI/CD or who want CI/CD and are moving to the cloud, 
without necessarily knowing anything about Kubernetes. Jenkins X builds on Jenkins with open source tools, 
promoting a Git branching and a repository model. A Jenkins distribution is used as the core CI/CD engine. 

[ The essentials from InfoWorld: Get started with CI/CD: Automating your application delivery with CI/CD pipelines. • 
5 common pitfalls of CI/CD—and how to avoid them. | Keep up with hot topics in programming with InfoWorld’s App Dev 
Report newsletter. ] Other features planned for the Jenkins X project include: 

Automation, with Jenkins defaulting to CI/CD pipelines for projects. Pull-request preview environments, 
to get feedback before changes are merged to the master version of a piece of software. Feedback is provided by 
Jenkins X as code is ready to be previewed. A set of environments for each team, with Jenkins X automating the 
management of environments and the promotion of new versions. More integrations with Git providers. Right now, 
Jenkins X supports GitHub but integrations are under consideration for Bitbucket and Gerrit Code Review. Jenkins X is 
a project of the newly formed Continuous Delivery Foundation, a Linux Foundation effort dedicated to continuous 
delivery and promoting an ecosystem of interoperable tools for software delivery. 

You can download the Jenkins X source code from the project’s GitHub page.

This story, "Jenkins tries to reinvent itself as cloud-native for Kubernetes" was originally published by InfoWorld.""",
            'date': '2019-03-19',
            'views': 0,
            'image_url': 'https://images.idgesg.net/images/article/2019/02/cloud_comput_connect_multiple_-100787052'
                         '-large.jpg',
            'category_fk': 2
        },
        {
            'title': 'Java, meet Kubernetes and serverless computing',
            'text': """Red Hat is looking to bring Java into more-modern computing paradigms by providing a tool 
            tuned to Kubernetes and serverless environments. 

Currently in beta, Red Hat’s open source Quarkus framework is aimed at a container-first, cloud-native world. It uses 
a unified reactive and imperative programming model to address distributed application architectures such as 
microservices and serverless. Java can be challenging to run in serverless environments, where compute services are 
called on demand. 

[ A developer’s guide: Serverless computing: AWS vs. Google Cloud vs. Microsoft Azure. | Then learn how to use 
Microsoft’s Azure Functions and how to use AWS Lambda for serverless computing. ] Red Hat says Quarkus will provide: 

Fast startup, in the range of tens of milliseconds, and automatic scaling for microservices on containers. 
Function-as-a-service (FaaS) and on-the-spot execution. Low-memory utilization to help optimize container density in 
microservices architecture deployments that require multiple containers. A smaller application and container image 
footprint. Configuration is done via a single property file. Code is streamlined for 80 percent common usages and 
provides flexibility for the other 20 percent of cases, Red Hat claims. Quarkus uses libraries including Eclipse 
MicroProfile and Vert.x, JPA/Hibernate, JAX_RS/RestEasy, and Netty. Quarkus has an extension framework for 
third-party framework authors to extend Quarkus. 

. Quarkus compiles to a native binary using Oracle’s GraalVM virtual machine, with apps able to run with 
significantly less RAM and start up quicker than a traditional app running on the JVM, benefitting serverless 
deployment. 

Developing with Quarkus requires a Java IDE, JDK 8 or later, Apache Maven 3.5.3 or later, and, for native 
applications, GraalVM. Apps are defined in a Maven POM XML file. 

This story, "Java, meet Kubernetes and serverless computing" was originally published by InfoWorld.""",
            'date': '2019-03-12',
            'views': 0,
            'image_url': 'https://images.idgesg.net/images/article/2018/06'
                         '/java_beans_grounds_coffee_binary_by_nathan_dumlao_cc0_via_unsplash_1200x800-100760556'
                         '-large.jpg',
            'category_fk': 2
        },
        {
            'title': 'Java thread sanitizer project proposed once again',
            'text': """Java developers would be clued in to race conditions in their projects, if a thread sanitizer 
            proposed comes to fruition. 

Project Tsan, proposed in the OpenJDK community, would explore and incubate a thread-sanitizing feature that would be 
integrated into the HotSpot JVM and the JVM tool interface. 

[ 15 Java frameworks that give developers a boost. • Which tools support Java’s new modularity features. | Keep up 
with hot topics in programming with InfoWorld’s App Dev Report newsletter. ] Thread sanitizing would let Java users 
see data race conditions. With a data race, multiple threads access shared data and try to change it at the same 
time, leading to erroneous and unexpected behaviors. 

The project was proposed by Google’s Jean Christophe Beyler, who said the Google platform team has worked on a thread 
sanitizer project internally. The Project Tsan thread-sanitizing proposal follows two previous proposals, 
also by Beyler: In November 2018, he proposed Atlantis, and in July 2018 he proposed Java Thread Sanitizer. 

The Tsan project would investigate how Google’s efforts in thread-sanitizing could be made general enough to be 
pushed into the mainline Java project. There is also the possibility that Google’s efforts would be rejected for 
being too specific. 

This story, "Java thread sanitizer project proposed once again" was originally published by InfoWorld.""",
            'date': '2019-02-19',
            'views': 0,
            'image_url': 'https://images.idgesg.net/images/article/2018/07/bicycle'
                         '-racing_binary_blur_compete_speed_fast_lead_by-maico-amorim-unsplash-100765878-large.jpg',
            'category_fk': 2
        },
        {
            'title': 'PuPPy Presents its 1st Annual Benefit featuring Guido van Rossum',
            'text': """
            Summary

PuPPy, Seattle's Puget Sound Programming Python user group, presents its 1st annual charity event. The event will 
feature the creators of C#, Java, Perl, Python, and TypeScript in a conversation about programming language design. 

The charity event brings together this unique group of computer science pioneers, unlike any event held before. These 
great minds come together for what will surely be a fantastic night of discussion, as the panel delves into the past 
and future of programming language creation. The event will attract innovators and engineers from Seattle, 
the nation’s fastest growing technology hub. 

The event is a benefit for CSforALL, a non-profit organization that represents more than 500 members who are 
educators, content providers, funders and researchers who share a vision for all students in the U.S. to learn 
computer science. CSforALL provides leadership and guidance that helps the K-12 education community implement 
computer science initiatives, draw from best practices and connect with national organizations to expand access to 
all students in the U.S. 

The event follows in the spirit and culture of PuPPy, the producers of this benefit, as an inclusive community. The 
very first PuPPy meeting 54 months ago was a mini-conference that featured discussions on allyship and helping more 
women join the ranks of software professionals. 

Event tickets and further details are available at: http://bdfl-gift.pspython.com.

Speakers

Cyrus Habib - Washington State Lieutenant Governor - Opening remarks Cyrus Habib was elected Washington State’s 16th 
Lieutenant Governor in November 2016 at the age of 35. He had previously been elected to the State House of 
Representatives in 2012 and the State Senate in 2014, where he was Democratic Whip and a member of the Democratic 
leadership team. As Lt. Governor, he is President of the State Senate, serves as Acting Governor whenever Governor 
Inslee leaves the state, and oversees an agency whose key issues include economic development, trade, and higher 
education. A three-time cancer survivor, Lt. Governor Habib has been fully blind since age eight. His parents 
immigrated to the U.S. from Iran before he was born, and he is the first and only Iranian-American to hold statewide 
elected office in the United States. 

Carol Willing - Moderator Carol Willing serves as a Steering Council member for Project Jupyter. She received the 
2017 ACM Software System Award for Jupyter's development. She is also a member of the inaugural Python Steering 
Council, a Python Software Foundation Fellow and former Director; a core developer on CPython, Jupyter, nteract, 
AnitaB.org’s open source projects, and PyLadies; a co-organizer of PyLadies San Diego and San Diego Python User 
Group; an independent developer of hardware and software. Weaving her love of art, music, and nature with wearable 
soft circuits, she is developing an open hardware project to assist an in-home caregiver with gentle, compassionate 
support of a loved one with Alzheimer’s. 

James Gosling - Java James A. Gosling, O.C., Ph.D. (born May 19, 1955, near Calgary, Alberta, Canada) is a famous 
software developer, best known as the father of the Java programming language. 

In 1977, James Gosling received a B.Sc in Computer Science from the University of Calgary. In 1983, he earned a Ph.D. 
in Computer Science from Carnegie Mellon University, and his doctoral thesis was titled "The Algebraic Manipulation 
of Constraints". While working towards his doctorate, he wrote a version of emacs (gosmacs), and before joining Sun 
Microsystems he built a multi-processor version of Unix[1] while at Carnegie Mellon University, as well as several 
compilers and mail systems. Since 1984, Gosling has been with Sun Microsystems. 

He is generally credited as the inventor of the Java programming language in 1991. He did the original design of Java 
and implemented its original compiler and virtual machine. For this achievement, he was elected to the United States 
National Academy of Engineering. He has also made major contributions to several other software systems, such as NeWS 
and Gosling Emacs. He also co-wrote the "bundle" program, a utility thoroughly detailed in Brian Kernighan and Rob 
Pike's book, "The Unix Programming Environment". 

Anders Hejlsberg - Turbo Pascal, C#, TypeScript Anders Hejlsberg is a Microsoft Technical Fellow and has been 
designing and implementing programming languages and development tools for over 35 years. Anders is the lead 
architect of the TypeScript open-source project and the original designer of the C# programming language. Before 
joining Microsoft in 1996, Anders was a Principal Engineer at Borland International. As one of the first employees of 
Borland, he was the original author of Turbo Pascal and later worked as the Chief Architect of the Delphi product 
line. Anders studied Engineering at the Technical University of Denmark. 

Guido van Rossum - Python Guido van Rossum is the creator of Python, one of the major programming languages on and 
off the web. Recently Guido retired as Benevolent Dictator For Life (“BDFL”) of Python, a title seemingly stolen from 
a Monty Python skit. Details of his decision were featured in an Economist article. Guido thankfully has joined the 
Python Steering Council. This five-person group will give guidance to the future roadmap of the Python programming 
language. 

Van Rossum moved from the Netherlands to the USA, in 1995. He met his wife after his move. Until July 2003 they lived 
in the northern Virginia suburbs of Washington, DC with their son Orlijn, who was born in 2001. They then moved to 
Silicon Valley where Guido worked for a variety of companies including Google in the past and currently at Dropbox (
spending 50% of his time on Python!). 

Larry Wall - Perl Larry Wall was educated at various places including the Cornish School of Music, the Seattle Youth 
Symphony, Seattle Pacific University, Multnomah School of the Bible, SIL International, U.C. Berkeley, 
and UCLA. Though trained primarily in music, chemistry, and linguistics, Larry has been working with computers for 
the last 40 years or so. He is most famous for writing rn, patch, and the Perl programming language, but prefers to 
think of himself as a cultural hacker whose vocation in life is to bring a bit of joy into the dreary existence of 
programmers. For various definitions of “work for”, Larry has worked for Seattle Pacific, MusiComedy Northwest, 
System Development Corporation, Burroughs, Unisys, the NSA, Telos, ConTel, GTE, JPL, NetLabs, Seagate, Tim O’Reilly, 
the Perl Foundation, Broadcom, and himself. He is currently serving as Artist in Residence for """,
            'date': '2019-03-27',
            'views': 0,
            'image_url': 'https://cdn-images-1.medium.com/max/1600/1*ZXixptvL4rzkx3EDuj38xw.jpeg',
            'category_fk': 1
        },
        {
            'title': 'Update on the Python in Education Proposal Phase',
            'text': """In January when we launched the Python in Education project, we were a bit too ambitious with 
            our timeline. Due to other commitments, we were not able to stick to the original time frame. 

Here is the revised timeline:

April 4 - May 9: Request for Proposals phase
May 10 - May 31: Review process
June 1: Notify the accepted proposals
June-August of 2019: Accepted proposal work begins


We'd also like to take this opportunity to inform everyone interested in submitting a proposal that we selected three 
categories we'd like to see proposals on. Additionally, we'd like to share the evaluation rubric we will use when 
reviewing each proposal. 

Proposal categories After reviewing all of the ideas we received in the first phase of this project, we have narrowed 
the scope of the proposals to: resources (curriculums, evaluations, studies, multidisciplinary projects) localization 
(translations, global currency, global timestamps, etc) mobile (development on mobile devices) We ask that if you are 
considering submitting a proposal that it fall into one of these broad categories. 

Evaluation rubric Every proposal we receive will be evaluated against this rubric. We are looking for proposals that 
adhere to the PSF's code of conduct, align with the PSF's mission, have international reach, are feasible, 
and pertain to underrepresented topics. 

If anyone has any questions, please contact us at edu-committee@python.org. """,
            'date': '2019-04-04',
            'views': 0,
            'image_url': 'https://4.bp.blogspot.com/-e6zsWUTw48o/XJqabIoCPRI/AAAAAAAAilE'
                         '/bfFlqmu8NzIQi4r8M__xFqEWJgzxWYCWwCLcBGAs/s320/CSforALL-logo.png',
            'category_fk': 1
        },
        {
            'title': 'Python 3.8.0a3 is now available for testing',
            'text': """
            Python 3.8.0a3 is now available for testing

Go get it here:
https://www.python.org/downloads/release/python-380a3/

The most visible change so far is probably the implementation of PEP 572: Assignment Expressions.  For a detailed 
list of changes, see: https://docs.python.org/3.8/whatsnew/changelog.html 

Python 3.8.0a3 is the third of four planned alpha releases of Python 3.8, the next feature release of Python.  During 
the alpha phase, Python 3.8 remains under heavy development: additional features will be added and existing features 
may be modified or deleted.  Please keep in mind that this is a preview release and its use is not recommended for 
production environments.  The last alpha release, Python 3.8.0a4, is planned for 2019-04-29. 

Thanks to all of the many volunteers who help make Python development and these releases possible!  Please consider 
supporting our efforts by volunteering yourself or through organization contributions to the Python Software 
Foundation. 
""",
            'date': '2019-03-26',
            'views': 0,
            'image_url': 'https://2.bp.blogspot.com/-Bhao0h7cGF0/TY-us8aVYCI/AAAAAAAAAYw/IhOLTFSw34E/s1600/python'
                         '-insider-header.png',
            'category_fk': 1
        },
        {
            'title': 'Python 3.7.3 is now available',
            'text': """
Python 3.7.3 is now available

Python 3.7.3 is now available. 3.7.3 is the next maintenance release of Python 3.7, the latest feature release of 
Python.  You can find the release files, a link to the changelog, and more information here: 
https://www.python.org/downloads/release/python-373/ 

See the What’s New In Python 3.7 document for more information about the many new features and optimizations included 
in the 3.7 series.  Detailed information about the changes made in 3.7.3 can be found in its change log. 

Thanks to all of the many volunteers who help make Python Development and these releases possible!  Please consider 
supporting our efforts by volunteering yourself or through organization contributions to the Python Software 
Foundation.""",
            'date': '2019-03-25',
            'views': 0,
            'image_url': 'https://2.bp.blogspot.com/-Bhao0h7cGF0/TY-us8aVYCI/AAAAAAAAAYw/IhOLTFSw34E/s1600/python'
                         '-insider-header.png',
            'category_fk': 1
        },
        {
            'title': 'Introductory workshop added - running in parallel on Monday',
            'text': """We're pleased to announce that we're adding another workshop track, to be led by Tristan 
            Brindle. But this workshop will run concurrently with the main conference on Monday - and will be an 
            intensive introductory course for C++ beginners. 

If you're coming to C++ from another language - or used to use it years ago and need a refresher - this could be just 
the course for you! Of course you'll be missing a big chunk of the conference on Monday (10:45 - 16:00 - so you'll 
still get the keynote, plenary and lighting talks) - but you'll get the whole of Tuesday, and only need a main 
conference ticket - no workshop ticket required. If you don't want to stay for Tuesday you can buy a one day ticket. 



Tristan is the main instructor at C++ London Uni), where he has been helping beginners learn C++, weekly, for over a 
year. 

After Monday 28th the main conference prices go up to Last Minute prices. In recognition of the fact that this 
workshop is being added so late, you can use the following coupon code to get standard rate prices (for both 2-day 
and single day admission). 

INITIALCPP2019
However you will, then, need to attend the workshop (except the first session)!""",
            'date': '2019-01-26',
            'views': 0,
            'image_url': 'https://cpponsea.uk/assets/cpplondonuni.jpg',
            'category_fk': 3
        },
        {
            'title': 'Videos are now being released',
            'text': """After a fantastic conference last week we're now starting to process and upload the videos to 
            YouTube. We have a channel on YouTube you can subscribe to, or keep checking back to see the latest 
            videos. Please do share them around! 

One of the most talked about presentations from the conference - and the video widely requested - was Kate Gregory's 
opening Keynote: "Oh, the Humanity!" and that was in the first batch of uploads. 

Our video team is working tirelessly to keep adding more videos over the few days to a week or so.""",
            'date': '2019-02-15',
            'views': 0,
            'image_url': 'https://cpponsea.uk/assets/ohthehumanity-thumbnail.jpg',
            'category_fk': 3
        }
    ]


def get_sample_categories():
    return [
        {
            'name': 'Python',
            'image_url': 'https://python.rs/pylogo.png',
            'description':
                """Python (найчастіше вживане прочитання — «Па́йтон», запозичено назву[5] з британського шоу Монті 
                Пайтон) — інтерпретована об\' єктно - орієнтована мова програмування високого рівня зі строгою 
                динамічною типізацією.[6] Розроблена в 1990 році Гвідо ван Россумом.Структури даних високого рівня 
                разом із динамічною семантикою та динамічним зв 'язуванням роблять її привабливою для швидкої 
                розробки програм, а також як засіб поєднування наявних компонентів. Python підтримує модулі та пакети 
                модулів, що сприяє модульності та повторному використанню коду. Інтерпретатор Python та стандартні 
                бібліотеки доступні як у скомпільованій, так і у вихідній формі на всіх основних платформах. В мові 
                програмування Python підтримується кілька парадигм програмування, зокрема: об\'єктно - орієнтована, 
                процедурна, функціональна та аспектно - орієнтована. """
        },
        {
            'name': 'Java',
            'image_url': 'https://cdn.lynda.com/course/184457/184457-636806635954727169-16x9.jpg',
            'description':
                """Java (вимовляється Джава[4]) — об'єктно-орієнтована мова програмування, випущена 1995 року 
                компанією «Sun Microsystems» як основний компонент платформи Java. З 2009 року мовою займається 
                компанія «Oracle», яка того року придбала «Sun Microsystems». В офіційній реалізації Java-програми 
                компілюються у байт-код, який при виконанні інтерпретується віртуальною машиною для конкретної 
                платформи. 
    
    «Oracle» надає компілятор Java та віртуальну машину Java, які задовольняють специфікації Java Community Process, 
    під ліцензією GNU General Public License. 
    
    Мова значно запозичила синтаксис із C і C++. Зокрема, взято за основу об'єктну модель С++, проте її модифіковано. 
    Усунуто можливість появи деяких конфліктних ситуацій, що могли виникнути через помилки програміста та полегшено 
    сам процес розробки об'єктно-орієнтованих програм. Ряд дій, які в С/C++ повинні здійснювати програмісти, 
    доручено віртуальній машині. Передусім Java розроблялась як платформо-незалежна мова, тому вона має менше 
    низькорівневих можливостей для роботи з апаратним забезпеченням, що в порівнянні, наприклад, з C++ зменшує 
    швидкість роботи програм. За необхідності таких дій Java дозволяє викликати підпрограми, написані іншими мовами 
    програмування. 
    
    Java вплинула на розвиток J++[en], що розроблялась компанією «Microsoft». Роботу над J++ було зупинено через 
    судовий позов «Sun Microsystems», оскільки ця мова програмування була модифікацією Java. Пізніше в новій 
    платформі «Microsoft» .NET випустили J#, щоб полегшити міграцію програмістів J++ або Java на нову платформу. З 
    часом нова мова програмування С# стала основною мовою платформи, перейнявши багато чого з Java. J# востаннє 
    включався в версію Microsoft Visual Studio 2005. Мова сценаріїв JavaScript має схожу із Java назву і синтаксис, 
    але не пов'язана із Java. """
        },
        {
            'name': 'C++',
            'image_url': 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/titleShadow-1024x341.png',
            'description':
                """C++ (Сі-плюс-плюс) — мова програмування високого[1][2] рівня з підтримкою кількох парадигм 
                програмування: об'єктно-орієнтованої, узагальненої та процедурної. Розроблена Б'ярном Страуструпом (
                англ. Bjarne Stroustrup) в AT&T Bell Laboratories (Мюррей-Хілл, Нью-Джерсі) 1979 року та початково 
                отримала назву «Сі з класами». Згодом Страуструп перейменував мову на C++ у 1983 р. Базується на мові 
                С. Вперше описана стандартом ISO/IEC 14882:1998, найбільш актуальним же є стандарт ISO/IEC 
                14882:2014.[3] 
    
    У 1990-х роках С++ стала однією з найуживаніших мов програмування загального призначення. Мову використовують для 
    системного програмування, розробки програмного забезпечення, написання драйверів, потужних серверних та 
    клієнтських програм, а також для розробки розважальних програм, наприклад, відеоігор. С++ суттєво вплинула на 
    інші популярні сьогодні мови програмування: С# та Java. """
        }
    ]
