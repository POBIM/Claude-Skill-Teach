const pptxgen = require('pptxgenjs');
const html2pptx = require('./../../.claude/skills/pptx/scripts/html2pptx.js');
const path = require('path');

async function createPresentation() {
    try {
        const pptx = new pptxgen();
        pptx.layout = 'LAYOUT_16x9';
        pptx.author = 'Claude Code';
        pptx.title = 'Claude Code Skills - วิธีการสร้างและการเทรน';
        pptx.subject = 'Skill Training with BOQ Example';

        const baseDir = path.dirname(__filename);

        // Slide 1: Title
        console.log('Creating slide 1: Title...');
        await html2pptx(path.join(baseDir, 'slide1_title.html'), pptx);

        // Slide 2: Overview
        console.log('Creating slide 2: Overview...');
        await html2pptx(path.join(baseDir, 'slide2_overview.html'), pptx);

        // Slide 3: BOQ Features
        console.log('Creating slide 3: BOQ Features...');
        await html2pptx(path.join(baseDir, 'slide3_boq_features.html'), pptx);

        // Slide 4: Creation Overview
        console.log('Creating slide 4: Creation Overview...');
        await html2pptx(path.join(baseDir, 'slide4_creation_overview.html'), pptx);

        // Slide 5: Folder Structure
        console.log('Creating slide 5: Folder Structure...');
        await html2pptx(path.join(baseDir, 'slide5_folder_structure.html'), pptx);

        // Slide 6: Core Scripts
        console.log('Creating slide 6: Core Scripts...');
        await html2pptx(path.join(baseDir, 'slide6_core_scripts.html'), pptx);

        // Slide 7: Metadata
        console.log('Creating slide 7: Metadata...');
        await html2pptx(path.join(baseDir, 'slide7_metadata.html'), pptx);

        // Slide 8: BOQ Example
        console.log('Creating slide 8: BOQ Example...');
        await html2pptx(path.join(baseDir, 'slide8_boq_example.html'), pptx);

        // Slide 9: Best Practices
        console.log('Creating slide 9: Best Practices...');
        await html2pptx(path.join(baseDir, 'slide9_best_practices.html'), pptx);

        // Slide 10: Usage
        console.log('Creating slide 10: Usage...');
        await html2pptx(path.join(baseDir, 'slide10_usage.html'), pptx);

        // Slide 11: Summary
        console.log('Creating slide 11: Summary...');
        await html2pptx(path.join(baseDir, 'slide11_summary.html'), pptx);

        // Save presentation
        const outputFile = path.join(baseDir, 'Claude_Code_Skills_Training.pptx');
        await pptx.writeFile({ fileName: outputFile });
        console.log(`\nPresentation created successfully: ${outputFile}`);

    } catch (error) {
        console.error('Error creating presentation:', error);
        process.exit(1);
    }
}

createPresentation();
