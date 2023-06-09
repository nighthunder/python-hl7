<h1>Using HL7 in python</h1>

```
pip install -r requirements.txt
```

<p>At documentation can be found references to the modules.</p>

<h2>What's HL7? </h2>

<p>Health Level Seven (HL7) is a set of international standards for the interchange of electronic health information. An HL7 message is a unit of communication in these systems and is structured as a sequence of segments, each of which provides a different category of information. Here's a brief overview of the HL7 message structure:</p>

<ol>
<li>Segment: A segment is a logical grouping of data fields. Each segment starts with a three-letter code that identifies the segment type. For example, the PID segment includes patient identification information. Each segment is on a new line.</li>

<li>Field: Each segment is divided into fields, separated by a delimiter (usually a pipe character "|"). The first field is always the segment type. Subsequent fields are specific to the segment type. For example, in the PID segment, there might be fields for patient ID, patient name, date of birth, etc.</li>

<li>Component: Fields can further be divided into components, which are sub-parts of a field. Components are typically separated by a caret ("^"). For example, a patient's name might be divided into components for first name, last name, and middle initial.</li>

<li>Sub-component: Sub-components are the smallest unit of data in an HL7 message. They are parts of a component and are typically separated by an ampersand ("&").</li>

<li>Repetition: Some fields are repeatable, which means they can appear more than once in a segment. Repeatable fields are typically separated by a tilde ("~").</li>

</ol>