const pptxgen = require('pptxgenjs');
const html2pptx = require('D:\\Git\\Claude Skill Teach\\.claude\\skills\\pptx\\scripts\\html2pptx');
const path = require('path');

async function createPresentation() {
    const pptx = new pptxgen();
    pptx.layout = 'LAYOUT_16x9';
    pptx.author = 'Claude Skills Tutorial';
    pptx.title = 'สร้าง Claude Skills สำหรับงานก่อสร้าง';
    pptx.subject = 'Tutorial on creating Claude Skills for construction work';

    const slidesDir = 'D:\\Git\\Claude Skill Teach\\workspace\\claude-skills-presentation';

    // Slide 1: Title
    console.log('Creating slide 1: Title...');
    await html2pptx(path.join(slidesDir, 'slide1-title.html'), pptx);

    // Slide 2: What is Claude Skill
    console.log('Creating slide 2: What is Claude Skill...');
    await html2pptx(path.join(slidesDir, 'slide2-what-is-skill.html'), pptx);

    // Slide 3: Why Construction
    console.log('Creating slide 3: Why Construction...');
    await html2pptx(path.join(slidesDir, 'slide3-why-construction.html'), pptx);

    // Slide 4: Examples
    console.log('Creating slide 4: Examples...');
    await html2pptx(path.join(slidesDir, 'slide4-examples.html'), pptx);

    // Slide 5: How to Command
    console.log('Creating slide 5: How to Command...');
    await html2pptx(path.join(slidesDir, 'slide5-how-to-command.html'), pptx);

    // Slide 6: Steps
    console.log('Creating slide 6: Steps...');
    await html2pptx(path.join(slidesDir, 'slide6-steps.html'), pptx);

    // Slide 7: File Structure
    console.log('Creating slide 7: File Structure...');
    await html2pptx(path.join(slidesDir, 'slide7-structure.html'), pptx);

    // Slide 8: BOQ Demo
    console.log('Creating slide 8: BOQ Demo...');
    await html2pptx(path.join(slidesDir, 'slide8-boq-demo.html'), pptx);

    // Slide 9: DXF Demo
    console.log('Creating slide 9: DXF Demo...');
    await html2pptx(path.join(slidesDir, 'slide9-dxf-demo.html'), pptx);

    // Slide 10: Tips
    console.log('Creating slide 10: Tips...');
    await html2pptx(path.join(slidesDir, 'slide10-tips.html'), pptx);

    // Slide 11: Summary
    console.log('Creating slide 11: Summary...');
    await html2pptx(path.join(slidesDir, 'slide11-summary.html'), pptx);

    // Save presentation
    const outputPath = path.join(slidesDir, 'Claude-Skills-Construction.pptx');
    await pptx.writeFile({ fileName: outputPath });
    console.log(`\nPresentation created successfully: ${outputPath}`);
}

createPresentation().catch(err => {
    console.error('Error creating presentation:', err);
    process.exit(1);
});
